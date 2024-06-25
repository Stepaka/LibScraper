from bs4 import BeautifulSoup
import os
import pandas as pd
import re

class HTMLParser:
    def __init__(self):
        self.data_frame = {}
        self.lineEdit_link_parse = ''
    
    def extract_data_from_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        tables = soup.find_all('table', {'cellspacing': '1', 'cellpadding': '3', 'bgcolor': '#ffffff', 'id': 'restab'})

        all_data = []

        for table in tables:
            rows = table.find_all('tr', {'valign': 'middle', 'bgcolor': ['#f5f5f5', '#ffffff']})

            for row in rows:
                columns = row.find_all(['td', 'th'])

                number = columns[0].find('font', {'color': '#00008f'}).b.text if columns[0].find('font', {'color': '#00008f'}) else None
                publication = columns[1].find('a').b.text if columns[1].find('a') and columns[1].find('a').b else None
                link = columns[1].find('a')['href'] if columns[1].find('a') else None
                author = columns[1].find('i').text if columns[1].find('i') else None

                journal_info = columns[1].find('a', href=lambda x: x and '/contents.asp?id=' in x)
                if journal_info:
                    journal = journal_info.text
                    journal_link = journal_info['href']
                else:
                    journal = None
                    journal_link = None

                issue_info = columns[1].find_all('a', string=lambda x: x and '№' in x)
                if issue_info:
                    issue_number = issue_info[-1].text
                    issue_link = issue_info[-1]['href']
                else:
                    issue_number = None
                    issue_link = None

                citation = columns[2].text if columns[2] else None

                year_match = re.search(r'\d{4}', publication)
                if year_match:
                    year = year_match.group()
                else:
                    year_info = re.search(r'\b\d{4}\b', columns[1].text)
                    year = year_info.group() if year_info else None
                
                all_data.append([number, publication, link, author, journal, journal_link, issue_number, issue_link, citation, year])

        return all_data

    def parse_basic(self, search_texts):
        for search_text in search_texts:
            print(search_text)
            all_data = []

            output_folder = f'{search_text}'
            for filename in os.listdir(output_folder):
                if filename.endswith(".html"):
                    input_file_path = os.path.join(output_folder, filename)

                    with open(input_file_path, 'r', encoding='utf-8') as file:
                        html_content = file.read()

                    table_data = self.extract_data_from_html(html_content)
                    all_data.extend(table_data)

            columns = ['№', 'Публикация', 'Ссылка', 'Автор', 'Журнал', 'Ссылка_на_журнал', 'Номер_журнала', 'Ссылка_на_номер_журнала', 'Цит.', 'Год']
            df = pd.DataFrame(all_data, columns=columns)
            df['Ссылка'] = 'https://www.elibrary.ru/' + df['Ссылка']
            df['Ссылка_на_журнал'] = 'https://www.elibrary.ru/' + df['Ссылка_на_журнал']
            df['Ссылка_на_номер_журнала'] = 'https://www.elibrary.ru/' + df['Ссылка_на_номер_журнала']

            df.replace(regex=[r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F-\x9F]'], value='', inplace=True)

            output_xlsx_filename = f'{search_text}/output.xlsx'
            df.to_excel(output_xlsx_filename, index=False)
            self.data_frame[search_text] = df

    def excel_to_dataframe(self, file_path):
        try:
            # Чтение данных из Excel файла в DataFrame
            df = pd.read_excel(file_path)
            return df
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None


    def list_to_dict_with_colon_separator(self, lst):
        result_dict = {}
        for item in lst:
            key_value_pair = item.split(':', 1)  # Разделяем строку на две части по первому встреченному ":"
            if len(key_value_pair) == 2:  # Если после разделения получили две части
                key, value = key_value_pair[0], key_value_pair[1].strip()  # Разделяем на ключ и значение
            else:
                key, value = key_value_pair[0], "-"  # Если после разделения получили только одну часть, то значение "-"
            result_dict[key.strip()] = value  # Удаляем лишние пробелы и добавляем в словарь
        return result_dict

    def extract_text_from_selectors(self, html_content, selector_dict):
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Итерируемся по элементам словаря
        for key, selector in selector_dict.items():
            # Находим элемент по CSS-селектору
            element = soup.select_one(selector)
            # Если элемент найден, забираем его текст и заменяем селектор в словаре
            if element:
                selector_dict[key] = element.get_text(strip=True)
            # Иначе заменяем значение на "-"
            else:
                selector_dict[key] = "-"

        # Возвращаем обновленный словарь
        return selector_dict


    def extract_text_detailed(self, html_content):
        all_cell_texts = []
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Находим целевую таблицу
        target_table = soup.select_one(
            'body > table > tbody > tr > td > table:nth-child(1) > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(1)'
        )

        if target_table:
            # Список строк, по которым будем искать
            target_strings = [
                "Рубрика OECD:",
                "Рубрика ASJC:",
                "Рубрика ГРНТИ:",
                "Специальность ВАК:"
            ]

            # Находим все изображения с указанными классами в целевой таблице
            img_elements = target_table.find_all('img', class_='imghelp help')

            # Извлекаем родительский элемент <td> для каждого изображения
            td_elements = [img.parent for img in img_elements]

            # Получаем текст из каждого элемента <td>
            for td in td_elements:
                text_td = td.get_text(strip=True).replace('\xa0', ' ')
                next_sibling = td.find_next_sibling('td')
                text_next_sibling = next_sibling.get_text(strip=True) if next_sibling else ""
                if text_td in target_strings:
                    all_cell_texts.append(text_td + text_next_sibling)
                else:
                    all_cell_texts.append(text_td)

        return self.list_to_dict_with_colon_separator(all_cell_texts)

    def parse_detailed(self, search_texts, data):
        for search_text in search_texts:
            # Путь к директории с файлами
            directory = f'{search_text}'

            # Создаем пустой DataFrame для хранения данных
            df = pd.DataFrame()

            # Проходимся по всем файлам в директории
            for filename in os.listdir(directory):
                if filename.endswith('.html'):
                    # Открываем файл и считываем его содержимое
                    file_path = os.path.join(directory, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        html_content = file.read()
                    xpath_dict = data.copy()
                    detailed = self.extract_text_detailed(html_content)
                    result_dict = self.extract_text_from_selectors(html_content, xpath_dict)
                    result_dict.update(detailed)

                    # Добавляем данные в DataFrame
                    df = df._append(result_dict, ignore_index=True)

            # Сохраняем DataFrame в файл Excel
            output_xlsx_filename = f'{search_text}/output_detailed.xlsx'
            # Удаление недопустимых символов из значений DataFrame
            df_cleaned = df.applymap(lambda x: ''.join([c for c in str(x) if c.isprintable()]))
            # Сохранение в Excel
            df_cleaned.to_excel(output_xlsx_filename, index=False, engine='openpyxl')

        return df
    
    def generate_common_selector(self, selector1, selector2):
        # Разбиваем селекторы на части
        parts1 = selector1.split('>')
        parts2 = selector2.split('>')
        # Ищем общий путь, начиная с конца
        common_parts = []
        for part1, part2 in zip(reversed(parts1), reversed(parts2)):
            if part1.strip() == part2.strip():
                common_parts.append(part1)
            else:
                pass

        # Формируем общий селектор из найденной общей части пути
        common_selector = '>'.join(reversed(common_parts)).strip()
        return common_selector

    def extract_text_for_parser_table(self, html_content, selector_dict, selector_table='#restab'):
        # Создаем объект BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Находим таблицу по селектору
        table = soup.select_one(selector_table)
        if not table:
            return {key: ["-"] * 1 for key in selector_dict.keys()}

        result_dict = {key: [] for key in selector_dict.keys()}

        # Итерируемся по элементам словаря
        for key, selector in selector_dict.items():
            common_selector = self.generate_common_selector(selector[0], selector[1])
            # Находим элементы по CSS-селектору
            elements = table.select(common_selector)
            # Проверяем тип данных и обрабатываем в зависимости от него
            for element in elements:
                if element:
                    if selector[2] == 'Text':
                        result_dict[key].append(element.get_text(strip=True))
                    elif selector[2] == 'Link':
                        result_dict[key].append(self.lineEdit_link_parse + element.get('href', '-'))
                    elif selector[2] == 'Img':
                        result_dict[key].append(element.get('src', '-'))
                else:
                    result_dict[key].append("-")

        # Приводим все списки к одинаковой длине
        max_length = max(len(values) for values in result_dict.values())
        for key in result_dict.keys():
            while len(result_dict[key]) < max_length:
                result_dict[key].append("-")

        return result_dict

    def parser_table(self, search_texts, data):
        for search_text in search_texts:
            # Путь к директории с файлами
            directory = f'{search_text}'

            # Создаем пустой DataFrame для хранения данных
            df = pd.DataFrame()

            # Проходимся по всем файлам в директории
            for filename in os.listdir(directory):
                if filename.endswith('.html'):
                    # Открываем файл и считываем его содержимое
                    file_path = os.path.join(directory, filename)
                    with open(file_path, "r", encoding="utf-8") as file:
                        html_content = file.read()
                    xpath_dict = data.copy()
                    result_dict = self.extract_text_for_parser_table(html_content, xpath_dict)

                    # Преобразуем result_dict в DataFrame и добавляем в основной DataFrame
                    temp_df = pd.DataFrame(result_dict)
                    df = pd.concat([df, temp_df], ignore_index=True)

            # Сохраняем DataFrame в файл Excel
            output_xlsx_filename = f'{search_text}/output_table.xlsx'
            # Удаление недопустимых символов из значений DataFrame
            df_cleaned = df.applymap(lambda x: ''.join([c for c in str(x) if c.isprintable()]))
            # Сохранение в Excel
            df_cleaned.to_excel(output_xlsx_filename, index=False, engine='openpyxl')

        return df