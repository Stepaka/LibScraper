import glob
import os
import random
import threading
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.common import exceptions
from concurrent.futures import ThreadPoolExecutor
from parser_class import HTMLParser
from scraper_class import WebScraper
import pandas as pd
import shutil
import os
import pickle
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtWidgets
from PIL import Image, ImageDraw

from gui import *
import sys


class UserSession:
    def __init__(self):
        self.data_frame = {}
        self.scraper = WebScraper(ui.name_project_line.text(), self.data_frame)
        self.parser = HTMLParser()
        self.directory_scrape = None
        self.directory_parse = None
        self.driver = None
        self.name_project = None
        self.path_project = None
        self.cookie_path = ''
        self.cookie_use = False
        self.proxy_path = ''
        self.proxy_use = False
        self.url_main = ''
        self.options = uc.ChromeOptions()
        self.count_page = 0
        self.active_threads = []
        self.scrapers = {}

    def path_to_parse(self):
        try:
            self.directory_parse = QFileDialog.getExistingDirectory(caption='Select Directory')
            self.set_history(self.directory_parse)
            print(self.directory_parse)
        except Exception as e:
            print('ERROR path_to_parse:', e)

    def path_to_scrape(self):
        self.name_project = ui.name_project_line.text()
        try:
            self.directory_scrape = QFileDialog.getExistingDirectory(caption='Select Directory')
            self.path_project = self.directory_scrape + "/" + self.name_project
            self.set_history(self.path_project)
            print(self.path_project)
        except Exception as e:
            print('ERROR path_to_scrape:', e)

    def start_parse(self):
        if self.directory_parse:
            self.set_history("Parse start")
            self.parser.lineEdit_link_parse = ui.lineEdit_link_parse.text()
            if ui.parser_settings.currentIndex() == 0:
                table = ui.tableWidget_page
                if table:
                    data = {}
                    for row in range(table.rowCount()):
                        key_item = table.item(row, 0)
                        value_item = table.item(row, 1)
                        if key_item is not None and value_item is not None and (key_item.text() != '') and (value_item.text() != ''):
                            key = key_item.text()
                            value = value_item.text()
                            data[key] = value
                    self.parser.parse_detailed([self.directory_parse], data)
                    if ui.delete_html.isChecked():
                        self.delete_html_files(self.directory_parse)
                else:
                    self.set_history("Table not found in the current tab")
            elif ui.parser_settings.currentIndex() == 1:
                table = ui.tableWidget_table
                if table:
                    data = {}
                    for row in range(table.rowCount()):
                        key_item = table.item(row, 0)
                        value_item_1 = table.item(row, 1)
                        value_item_2 = table.item(row, 2)
                        if key_item is not None and value_item_1 is not None and value_item_2 is not None and (key_item.text() != '') and (value_item_1.text() != '') and (value_item_2.text() != ''):
                            key = key_item.text()
                            value_1 = value_item_1.text()
                            value_2 = value_item_2.text()
                            type  = table.cellWidget(row, 3).currentText()
                            data[key] = [value_1, value_2, type]
                    self.parser.parser_table([self.directory_parse], data)
                    if ui.delete_html.isChecked():
                        self.delete_html_files(self.directory_parse)
                else:
                    self.set_history("Table not found in the current tab")
            self.set_history("Parse complite")
        else:
            self.set_history("No directory selected for parsing")

    def monitor_threads(self):
        while True:
            for thread in self.active_threads:
                if thread and not thread.is_alive():
                    thread.join()
                    self.active_threads.remove(thread)
                    if thread in self.scrapers:
                        del self.scrapers[thread]  # удаляем объект scraper из словаря
                    self.count_page -= 1
                    print(f"Number of pages after closing: {self.count_page}")
                    print(self.active_threads)
            time.sleep(1)

    def start_scrape(self):
        if self.path_project:
            for i in range(ui.thread_box.value()):
                if self.count_page<4:
                    self.set_history(f"Open window {self.count_page}")
                    self.scraper = WebScraper([self.path_project+ f"/tread_{self.count_page}"], self.data_frame)
                    self.scraper.name_column = ui.link_nex_page_line_2.text()
                    self.scraper.times = ui.speed_slider.value()
                    self.scraper.next_page=ui.link_nex_page_line.text()
                    self.url_main = ui.lineEdit_start_page.text()
                    self.scraper.url = self.url_main
                    self.options = uc.ChromeOptions()
                    if self.proxy_use:
                        self.proxy_options()
                    if ui.scraper_settings.currentIndex() == 0:
                        thread = threading.Thread(target=self.scraper.start, args=(self.options, 'find', self.scraper.times, self.cookie_path if self.cookie_use else ''))
                    elif ui.scraper_settings.currentIndex() == 1:
                        self.scraper.data_frame = self.data_frame
                        thread = threading.Thread(target=self.scraper.start, args=(self.options, 'read', self.scraper.times, self.cookie_path if self.cookie_use else ''))
                    self.scrapers[thread] = self.scraper
                    self.count_page += 1
                    thread.start()
                    self.active_threads.append(thread)
                    print(self.count_page)
                    time.sleep(2)
                else:self.set_history("Количество страниц может быть не больше 4")
        else:
            self.set_history("Scraper not initialized")

    def stop_thread(self, thread):
        if thread.is_alive():
            thread.join()  # Ожидание завершения потока
        self.set_history("Thread stopped")

    def excel_to_dataframe(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(caption='Select Excel File', filter='Excel Files (*.xls *.xlsx)')
            if file_path:
                # Чтение данных из Excel файла в DataFrame
                df = pd.read_excel(file_path)
                self.data_frame = df
                # return df
            else:
                self.set_history("No file selected")
                return None
        except Exception as e:
            print(f"excel_to_dataframe Ошибка при чтении файла: {e}")
            return None

    def use_cookie(self):
        self.cookie_use = ui.checkBox_use_cookie.isChecked()  # Изменяем состояние флага паузы при каждом вводе
        if self.cookie_use:
            print("True cookie")
        else: print("False cookie")
    
    def cookie_save(self):
        file_path, _ = QFileDialog.getSaveFileName(caption='Select File to Save', filter='Cookie Files (*.pkl)')
        if file_path:
            self.scraper.cookie_save(file_path)
            self.set_history("Cookie save")

    def cookie_load(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(caption='Select Cookie File', filter='Cookie Files (*.pkl)')
            if file_path:
                self.cookie_path = file_path
                self.set_history(self.cookie_path)
            else:
                print("No file selected")
                return None
        except Exception as e:
            self.set_history(f"cookie_load Ошибка при чтении файла: {e}")
            return None

    def Eparser(self):
        self.parser.parse_basic([self.directory_parse])

    def pause(self):
        for thread, scraper in self.scrapers.items():
            if thread.is_alive():
                scraper.pause()

    def time_set(self, Int):
        for thread, scraper in self.scrapers.items():
            if thread.is_alive():
                scraper.times = Int

    def use_proxy(self):
        self.proxy_use = ui.checkBox_use_proxy.isChecked()  # Изменяем состояние флага паузы при каждом вводе
        if self.proxy_use:
            print("True proxy")
        else: print("False proxy")

    def proxy_load(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(caption='Select Text File', filter='Text Files (*.txt)')
            if file_path:
                self.proxy_path = file_path
                self.set_history(self.proxy_path)
            else:
                print("No file selected")
                return None
        except Exception as e:
            self.set_history(f"proxy_load Ошибка при чтении файла: {e}")
            return None

    def proxy_options(self):
        try:
            proxy_list = list(map(str.rstrip, open(self.proxy_path).readlines()))
            print(proxy_list)
            if len(proxy_list)==1:
                proxy = proxy_list[0]
            elif ui.proxy_list_read.currentText()=="Случайный":
                proxy=random.choice(proxy_list)
            elif ui.proxy_list_read.currentText()=="По списку":
                proxy=proxy_list[self.count_page%3]
            ip, port, login, password = proxy.split(":")
            self.set_history(f"IP страницы: {ip} || Порт страницы: {port}")
            if proxy:
                self.options.add_argument(f'--proxy-server=http://{ip}:{port}')
                self.options.add_argument('--ignore-certificate-errors')
        except Exception as e:
            self.set_history(f"proxy_options Ошибка при чтении файла: {e}")
            return None

    def stop_all_processes(self, event):
        # Сохранить переменные в файл
        self.save_variables('variables.pkl')
        # Остановить все процессы, какие-либо закрытия соединений, очистить ресурсы и т. д.
        if self.scraper:
            self.scraper.stop()  # Приостановка скрапера, если он активен

        if self.driver:
            self.driver.quit()  # Закрытие драйвера браузера, если он активен

        sys.exit(0)  # Выход из приложения с кодом успешного завершения

    def set_history(self, text):
        print(text)
        current_text = ui.textEdit_history.toPlainText()
        new_text = text + "\n" + current_text
        ui.textEdit_history.setPlainText(new_text)

    def save_variables(self, file_path):
        try:
            with open(file_path, 'wb') as file:
                pickle.dump({
                    'data_frame': self.data_frame,
                    'cookie_path': self.cookie_path,
                    'cookie_use': self.cookie_use,
                    'proxy_path': self.proxy_path,
                    'proxy_use': self.proxy_use
                }, file)
            print("Variables saved successfully.")
        except Exception as e:
            self.set_history(f"Error while saving variables: {e}")

    def load_variables(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                variables = pickle.load(file)
                self.data_frame = variables.get('data_frame', {})
                self.cookie_path = variables.get('cookie_path', '')
                self.cookie_use = variables.get('cookie_use', False)
                self.proxy_path = variables.get('proxy_path', '')
                self.proxy_use = variables.get('proxy_use', False)
                if self.cookie_use:
                    ui.checkBox_use_cookie.click()
                if self.proxy_use:
                    ui.checkBox_use_proxy.click()
            print("Variables loaded successfully.")
        except Exception as e:
            self.set_history(f"Error while loading variables: {e}")

    def save_to_excel(self, table):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
            if not file_path:
                return  # Если пользователь закрыл диалог без выбора файла, просто возвращаемся
            # Получаем данные из таблицы
            data = []
            for row in range(table.rowCount()):
                row_data = []
                other_columns_non_empty = False
                for column in range(table.columnCount()):
                    if column == table.columnCount()-1:
                        widget = table.cellWidget(row, column)
                        if widget:
                            if other_columns_non_empty:
                                row_data.append(widget.currentText())
                            else:
                                row_data.append('')
                        else:
                            row_data.append('')
                    else:
                        item = table.item(row, column)
                        if item and item.text():
                            row_data.append(item.text())
                            other_columns_non_empty = True
                        else: row_data.append('')
                # Добавляем строку в список только если хотя бы одна ячейка кроме последней не пуста
                if other_columns_non_empty:
                    data.append(row_data)

            # Создаем DataFrame и сохраняем в Excel
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False, header=False, engine='openpyxl')
        except Exception as e:
            self.set_history(f"Ошибка сохраниения файла: {e}")
            return None

    def load_from_excel(self, table):
        try:
            file_path, _ = QFileDialog.getOpenFileName(caption='Select Excel File', filter='Excel Files (*.xls *.xlsx)')
            if file_path:
                # Загружаем данные из Excel
                df = pd.read_excel(file_path, header=None, engine='openpyxl')

                for row in range(len(df)):
                    for column in range(len(df.columns)):
                        if column == table.columnCount()-1:
                            combo = QtWidgets.QComboBox()
                            combo.addItems(["Text", "Link", "Img"])
                            combo.setCurrentText(str(df.iat[row, column]))
                            table.setCellWidget(row, column, combo)
                        else:
                            item = QtWidgets.QTableWidgetItem(str(df.iat[row, column]))
                            if item.text() == 'nan':
                                item.setText('')
                            table.setItem(row, column, item)
            else:
                self.set_history("No file selected")
                return None
        except Exception as e:
            self.set_history(f"load_from_excel Ошибка при чтении файла: {e}")
            return None

    def delete_html_files(self, folder_path):
        try:
            # Генерируем путь ко всем файлам .html в указанной папке
            html_files = glob.glob(os.path.join(folder_path, '*.html'))
            # Удаляем каждый файл
            for file_path in html_files:
                os.remove(file_path)
            print("Все файлы .html успешно удалены.")
        except Exception as e:
            print(f"Ошибка при удалении файлов: {e}")

if __name__ == "__main__":
    List = {}
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    for row in range(ui.tableWidget_table.rowCount()):
        combo = QtWidgets.QComboBox()
        combo.addItems(["Text", "Link", "Img"])
        ui.tableWidget_table.setCellWidget(row, 3, combo)
    for row in range(ui.tableWidget_page.rowCount()):
        combo = QtWidgets.QComboBox()
        combo.addItems(["Text", "Link", "Img"])
        ui.tableWidget_page.setCellWidget(row, 2, combo)
    ui.tableWidget_page.horizontalHeader().setVisible(True)
    ui.tableWidget_table.horizontalHeader().setVisible(True)

    MainWindow.show()

    session = UserSession()

    # # Загрузить переменные из файла
    session.load_variables('variables.pkl')

    directory_parse = ui.path_to_parse.clicked.connect(session.path_to_parse)
    ui.path_to_scrape.clicked.connect(session.path_to_scrape)
    ui.start_parse.clicked.connect(session.start_parse)
    ui.start_scrape.clicked.connect(session.start_scrape)
    ui.pause.clicked.connect(session.pause)
    ui.save_cookie.clicked.connect(session.cookie_save)
    ui.set_cookie.clicked.connect(session.cookie_load)
    ui.path_to_proxy.clicked.connect(session.proxy_load)
    ui.exel_to_dataframe.clicked.connect(session.excel_to_dataframe)
    ui.speed_slider.valueChanged['int'].connect(session.time_set)
    ui.elibrary_parse.clicked.connect(session.Eparser)
    ui.checkBox_use_cookie.stateChanged.connect(session.use_cookie)
    ui.checkBox_use_proxy.stateChanged.connect(session.use_proxy)
    ui.exel_for_page_save.clicked.connect(lambda checked, table=ui.tableWidget_page: session.save_to_excel(table))
    ui.exel_for_table_save.clicked.connect(lambda checked, table=ui.tableWidget_table: session.save_to_excel(table))
    ui.exel_for_page_load.clicked.connect(lambda checked, table=ui.tableWidget_page: session.load_from_excel(table))
    ui.exel_for_table_load.clicked.connect(lambda checked, table=ui.tableWidget_table: session.load_from_excel(table))

    # Подключите сигнал закрытия окна к методу остановки всех процессов
    MainWindow.closeEvent = lambda event: session.stop_all_processes(event)

    # Запуск мониторинга потоков
    monitor_thread = threading.Thread(target=session.monitor_threads, daemon=True)
    monitor_thread.start()

    sys.exit(app.exec_())