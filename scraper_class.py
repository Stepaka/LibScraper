import os
import time
import requests
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, WebDriverException
from concurrent.futures import ThreadPoolExecutor
import pickle
from selenium.common import exceptions
import parse_html
import threading  # Импортируем модуль threading для работы с потоками

class WebScraper:
    def __init__(self, search_texts, data_frame={}, url='https://elibrary.ru/', proxy_list_path='proxy.txt'):
        self.search_texts = search_texts
        self.data_frame = data_frame
        self.url = url
        self.running = True  # Флаг для отслеживания состояния работы скрепера
        self.paused = True  # Флаг для отслеживания состояния паузы
        self.times=5
        self.next_page = None
        self.name_column = ""
        self.driver = None
        self.api_key = None

    def toggle_checkbox(self, driver, checkbox_id, activate=True):
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, checkbox_id))
        )
        if activate and not checkbox.is_selected():
            checkbox.click()
        elif not activate and checkbox.is_selected():
            checkbox.click()

    def stop(self):
        self.running = False

    def pause(self):
        self.paused = not self.paused  # Изменяем состояние флага паузы при каждом вводе
        if self.paused:
            print("paused")
        else: print("go")

    def resume(self):
        self.paused = False

    def search_and_scrape(self, search_text, driver):
        page = 1
        output_folder = f'{search_text}'
        os.makedirs(output_folder, exist_ok=True)

        driver.get(self.url)
        page_content = driver.page_source

        output_filename = f'{output_folder}/output_page_{page}.html'
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(page_content)

        driver.implicitly_wait(10)

        while self.running:  # Проверяем флаг перед каждым переходом на следующую страницу
            try:
                # Пробуем получить заголовок текущего окна
                title = driver.title
            except WebDriverException:
                # Если возникает исключение, окно закрыто
                print('Окно браузера закрыто.')
                break
            # Пауза на 1 секунду перед следующей проверкой
            time.sleep(1)
            
            if self.paused:
                time.sleep(5)  # Если пауза активирована, делаем паузу и пропускаем итерацию
                continue

            try:
                next_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.next_page))
                )

                if next_button.is_enabled():
                    next_button.click()

                    driver.implicitly_wait(5)
                    time.sleep(self.times)
                    page += 1
                    page_content = driver.page_source

                    output_filename = f'{output_folder}/output_page_{page}.html'
                    with open(output_filename, 'w', encoding='utf-8') as file:
                        file.write(page_content)

                    print(f"NEXT PAGE {page}")
                else:
                    print("Next button is not clickable. Stopping search.")
                    break

            except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
                print("NOT found next page or TimeoutException")
                self.pause()

    def is_captcha_present(self, driver):
        try:
            # Замените 'captcha-element-selector' на реальный селектор элемента капчи
            driver.find_element(By.CSS_SELECTOR, 'captcha-element-selector')
            return True
        except NoSuchElementException:
            return False
    
    def solve_captcha(self, captcha_image_url):
        captcha_id = requests.post(
            'http://2captcha.com/in.php',
            data={'key': self.api_key, 'method': 'base64', 'body': captcha_image_url}
        ).text.split('|')[1]
        print(f"Captcha ID: {captcha_id}")

        while True:
            response = requests.get(f'http://2captcha.com/res.php?key={self.api_key}&action=get&id={captcha_id}').text
            if response == 'CAPCHA_NOT_READY':
                time.sleep(5)
                continue
            if 'OK|' in response:
                return response.split('|')[1]

    def wait_for_page_load(self, driver, timeout=30):
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script('return jQuery.active == 0') if d.execute_script('return typeof jQuery != "undefined"') else True
            )
        except TimeoutException:
            print("Page load timeout after waiting for document ready state and jQuery to become idle.")

    def scrape_links(self, search_text, driver):
        page = 1
        output_folder = f'{search_text}'
        os.makedirs(output_folder, exist_ok=True)

        df = self.data_frame
        if df is None:
            print(f"Data for '{search_text}' has not been scraped yet.")
            return
        links = df[self.name_column].tolist()
        for link in links:
            try:
                # Пробуем получить заголовок текущего окна
                title = driver.title
            except WebDriverException:
                # Если возникает исключение, окно закрыто
                print('Окно браузера закрыто.')
                break
            # Пауза на 1 секунду перед следующей проверкой
            time.sleep(1)
            if self.paused:
                time.sleep(5)
                continue

            if not self.running:  # Проверяем флаг running перед обработкой каждой ссылки
                break

            time.sleep(self.times)
            driver.get(link)
            if self.is_captcha_present(driver):
                print("CAPTCHA detected. Pausing...")
                self.pause()
                continue
            # if self.is_captcha_present(driver):
            #     print("CAPTCHA detected. Pausing...")
            #     captcha_image_url = driver.find_element(By.CSS_SELECTOR, 'captcha-image-selector').get_attribute('src')
            #     captcha_solution = self.solve_captcha(captcha_image_url)
            #     print(f"Captcha Solved: {captcha_solution}")
            #     driver.find_element(By.CSS_SELECTOR, 'captcha-input-selector').send_keys(captcha_solution)
            #     driver.find_element(By.CSS_SELECTOR, 'captcha-submit-selector').click()
            #     time.sleep(self.times)
            #     self.pause()

            # Ожидание полной загрузки страницы
            self.wait_for_page_load(driver)

            page_content = driver.page_source
            page += 1
            output_filename = f'{output_folder}/output_page_{page}.html'
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(page_content)

    def cookie_save(self, directory):
        pickle.dump( self.driver.get_cookies() , open(directory,"wb"))
        print("Cookies have been saved")


    def start(self, options, flag='find', times=5, cookie_path=''):
        self.times = times
        for search_text in self.search_texts:  # Мониторим состояние работы скрепера в цикле
            if not self.running:  # Если флаг running установлен в False, завершаем выполнение цикла
                break
            self.driver = uc.Chrome(options=options, use_subprocess=True)#.Firefox()
            self.driver.get(self.url)
            if cookie_path:
                cookies = pickle.load(open(cookie_path, "rb"))
                for cookie in cookies:
                    try:
                        self.driver.add_cookie(cookie)
                    except Exception as e:
                        print("cookie error:", e)
                time.sleep(self.times)
                self.driver.refresh()
            try:
                if flag=='find':
                    self.search_and_scrape(search_text, self.driver)
                if flag=='read':
                    self.scrape_links(search_text, self.driver)
            finally:
                self.driver.quit()
                print(f"Closed browser for {search_text}")
        print("Scraper finished")
        return 0


