from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(486, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.settings = QtWidgets.QTabWidget(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(0, 0, 501, 501))
        self.settings.setAutoFillBackground(False)
        self.settings.setObjectName("settings")
        self.Scraper = QtWidgets.QWidget()
        self.Scraper.setObjectName("Scraper")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Scraper)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 370, 371, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pause = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pause.setCheckable(True)
        self.pause.setChecked(True)
        self.pause.setObjectName("pause")
        self.horizontalLayout.addWidget(self.pause)
        self.start_scrape = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_scrape.setCheckable(True)
        self.start_scrape.setChecked(False)
        self.start_scrape.setObjectName("start_scrape")
        self.horizontalLayout.addWidget(self.start_scrape)
        self.name_project_line = QtWidgets.QLineEdit(self.Scraper)
        self.name_project_line.setGeometry(QtCore.QRect(50, 30, 361, 22))
        self.name_project_line.setObjectName("name_project_line")
        self.path_to_scrape = QtWidgets.QToolButton(self.Scraper)
        self.path_to_scrape.setGeometry(QtCore.QRect(50, 60, 151, 22))
        self.path_to_scrape.setCheckable(True)
        self.path_to_scrape.setChecked(False)
        self.path_to_scrape.setObjectName("path_to_scrape")
        self.speed_slider = QtWidgets.QSlider(self.Scraper)
        self.speed_slider.setGeometry(QtCore.QRect(50, 320, 371, 22))
        self.speed_slider.setAcceptDrops(False)
        self.speed_slider.setAutoFillBackground(True)
        self.speed_slider.setMaximum(60)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.thread_box = QtWidgets.QSpinBox(self.Scraper)
        self.thread_box.setGeometry(QtCore.QRect(150, 270, 41, 21))
        self.thread_box.setMinimum(1)
        self.thread_box.setMaximum(4)
        self.thread_box.setObjectName("thread_box")
        self.label_slider = QtWidgets.QLabel(self.Scraper)
        self.label_slider.setGeometry(QtCore.QRect(170, 300, 51, 21))
        self.label_slider.setObjectName("label_slider")
        self.label_value = QtWidgets.QLabel(self.Scraper)
        self.label_value.setGeometry(QtCore.QRect(80, 300, 91, 20))
        self.label_value.setObjectName("label_value")
        self.label_2 = QtWidgets.QLabel(self.Scraper)
        self.label_2.setGeometry(QtCore.QRect(50, 10, 231, 16))
        self.label_2.setObjectName("label_2")
        self.scraper_settings = QtWidgets.QTabWidget(self.Scraper)
        self.scraper_settings.setGeometry(QtCore.QRect(50, 100, 381, 141))
        self.scraper_settings.setObjectName("scraper_settings")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.link_nex_page_line = QtWidgets.QLineEdit(self.tab_2)
        self.link_nex_page_line.setGeometry(QtCore.QRect(10, 40, 351, 22))
        self.link_nex_page_line.setObjectName("link_nex_page_line")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label.setObjectName("label")
        self.scraper_settings.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.exel_to_dataframe = QtWidgets.QPushButton(self.tab_3)
        self.exel_to_dataframe.setGeometry(QtCore.QRect(10, 10, 121, 28))
        self.exel_to_dataframe.setCheckable(True)
        self.exel_to_dataframe.setObjectName("exel_to_dataframe")
        self.link_nex_page_line_2 = QtWidgets.QLineEdit(self.tab_3)
        self.link_nex_page_line_2.setGeometry(QtCore.QRect(10, 70, 351, 22))
        self.link_nex_page_line_2.setText("")
        self.link_nex_page_line_2.setObjectName("link_nex_page_line_2")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 211, 16))
        self.label_3.setObjectName("label_3")
        self.scraper_settings.addTab(self.tab_3, "")
        self.label_6 = QtWidgets.QLabel(self.Scraper)
        self.label_6.setGeometry(QtCore.QRect(70, 270, 81, 21))
        self.label_6.setObjectName("label_6")
        self.settings.addTab(self.Scraper, "")
        self.Parser = QtWidgets.QWidget()
        self.Parser.setObjectName("Parser")
        self.path_to_parse = QtWidgets.QToolButton(self.Parser)
        self.path_to_parse.setGeometry(QtCore.QRect(10, 10, 91, 22))
        self.path_to_parse.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.path_to_parse.setCheckable(True)
        self.path_to_parse.setObjectName("path_to_parse")
        self.start_parse = QtWidgets.QPushButton(self.Parser)
        self.start_parse.setGeometry(QtCore.QRect(30, 440, 151, 28))
        self.start_parse.setObjectName("start_parse")
        self.pushButton_top = QtWidgets.QPushButton(self.Parser)
        self.pushButton_top.setGeometry(QtCore.QRect(400, 440, 61, 21))
        self.pushButton_top.setObjectName("pushButton_top")
        self.elibrary_parse = QtWidgets.QPushButton(self.Parser)
        self.elibrary_parse.setGeometry(QtCore.QRect(120, 10, 93, 21))
        self.elibrary_parse.setObjectName("elibrary_parse")
        self.parser_settings = QtWidgets.QTabWidget(self.Parser)
        self.parser_settings.setGeometry(QtCore.QRect(10, 40, 461, 401))
        self.parser_settings.setObjectName("parser_settings")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_page = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_page.setGeometry(QtCore.QRect(0, 0, 451, 341))
        self.tableWidget_page.setRowCount(100)
        self.tableWidget_page.setColumnCount(3)
        self.tableWidget_page.setObjectName("tableWidget_page")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_page.setItem(6, 1, item)
        self.tableWidget_page.horizontalHeader().setVisible(False)
        self.tableWidget_page.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_page.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidget_page.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget_page.verticalHeader().setVisible(False)
        self.exel_for_page_load = QtWidgets.QPushButton(self.tab_4)
        self.exel_for_page_load.setGeometry(QtCore.QRect(0, 340, 151, 28))
        self.exel_for_page_load.setObjectName("exel_for_page_load")
        self.exel_for_page_save = QtWidgets.QPushButton(self.tab_4)
        self.exel_for_page_save.setGeometry(QtCore.QRect(150, 340, 151, 28))
        self.exel_for_page_save.setObjectName("exel_for_page_save")
        self.parser_settings.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_table = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_table.setGeometry(QtCore.QRect(0, 0, 451, 341))
        self.tableWidget_table.setRowCount(100)
        self.tableWidget_table.setColumnCount(4)
        self.tableWidget_table.setObjectName("tableWidget_table")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_table.setItem(6, 1, item)
        self.tableWidget_table.horizontalHeader().setVisible(False)
        self.tableWidget_table.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_table.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_table.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_table.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_table.verticalHeader().setVisible(False)
        self.selector_for_table = QtWidgets.QLineEdit(self.tab_5)
        self.selector_for_table.setEnabled(True)
        self.selector_for_table.setGeometry(QtCore.QRect(300, 340, 151, 31))
        self.selector_for_table.setObjectName("selector_for_table")
        self.exel_for_table_load = QtWidgets.QPushButton(self.tab_5)
        self.exel_for_table_load.setGeometry(QtCore.QRect(0, 340, 151, 28))
        self.exel_for_table_load.setObjectName("exel_for_table_load")
        self.exel_for_table_save = QtWidgets.QPushButton(self.tab_5)
        self.exel_for_table_save.setGeometry(QtCore.QRect(150, 340, 151, 28))
        self.exel_for_table_save.setObjectName("exel_for_table_save")
        self.parser_settings.addTab(self.tab_5, "")
        self.settings.addTab(self.Parser, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.save_cookie = QtWidgets.QPushButton(self.tab)
        self.save_cookie.setGeometry(QtCore.QRect(330, 20, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_cookie.sizePolicy().hasHeightForWidth())
        self.save_cookie.setSizePolicy(sizePolicy)
        self.save_cookie.setObjectName("save_cookie")
        self.path_to_proxy = QtWidgets.QToolButton(self.tab)
        self.path_to_proxy.setGeometry(QtCore.QRect(30, 20, 101, 31))
        self.path_to_proxy.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.path_to_proxy.setCheckable(True)
        self.path_to_proxy.setObjectName("path_to_proxy")
        self.set_cookie = QtWidgets.QPushButton(self.tab)
        self.set_cookie.setGeometry(QtCore.QRect(330, 70, 101, 31))
        self.set_cookie.setCheckable(True)
        self.set_cookie.setChecked(False)
        self.set_cookie.setObjectName("set_cookie")
        self.checkBox_use_cookie = QtWidgets.QCheckBox(self.tab)
        self.checkBox_use_cookie.setGeometry(QtCore.QRect(330, 120, 151, 20))
        self.checkBox_use_cookie.setObjectName("checkBox_use_cookie")
        self.lineEdit_start_page = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_start_page.setGeometry(QtCore.QRect(30, 340, 231, 22))
        self.lineEdit_start_page.setObjectName("lineEdit_start_page")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 320, 191, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 201, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_link_parse = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_link_parse.setGeometry(QtCore.QRect(30, 400, 231, 22))
        self.lineEdit_link_parse.setObjectName("lineEdit_link_parse")
        self.checkBox_use_proxy = QtWidgets.QCheckBox(self.tab)
        self.checkBox_use_proxy.setGeometry(QtCore.QRect(30, 120, 71, 20))
        self.checkBox_use_proxy.setObjectName("checkBox_use_proxy")
        self.delete_html = QtWidgets.QCheckBox(self.tab)
        self.delete_html.setGeometry(QtCore.QRect(30, 280, 151, 31))
        self.delete_html.setObjectName("delete_html")
        self.proxy_list_read = QtWidgets.QComboBox(self.tab)
        self.proxy_list_read.setGeometry(QtCore.QRect(30, 70, 101, 31))
        self.proxy_list_read.setObjectName("proxy_list_read")
        self.proxy_list_read.addItem("")
        self.proxy_list_read.addItem("")
        self.settings.addTab(self.tab, "")
        self.textEdit_history = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_history.setGeometry(QtCore.QRect(30, 500, 441, 51))
        self.textEdit_history.setObjectName("textEdit_history")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.settings.setCurrentIndex(0)
        self.scraper_settings.setCurrentIndex(0)
        self.parser_settings.setCurrentIndex(0)
        self.pushButton_top.clicked.connect(self.tableWidget_page.scrollToTop) # type: ignore
        self.speed_slider.valueChanged['int'].connect(self.label_slider.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LibScraper"))
        self.pause.setText(_translate("MainWindow", "Pause"))
        self.start_scrape.setText(_translate("MainWindow", "Open window"))
        self.path_to_scrape.setText(_translate("MainWindow", "Место сохранения"))
        self.label_slider.setText(_translate("MainWindow", "0"))
        self.label_value.setText(_translate("MainWindow", "Задержка (с) :"))
        self.label_2.setText(_translate("MainWindow", "Название проекта"))
        self.link_nex_page_line.setText(_translate("MainWindow", "//*[@id=\"thepage\"]/table/tbody/tr/td/table/tbody/tr/td[4]/table/tbody/tr[3]/td[2]/a[text()=\"Следующая страница\"]"))
        self.label.setText(_translate("MainWindow", "Selector на следующую страницу"))
        self.scraper_settings.setTabText(self.scraper_settings.indexOf(self.tab_2), _translate("MainWindow", "Selector"))
        self.exel_to_dataframe.setText(_translate("MainWindow", "Загрузить excel"))
        self.label_3.setText(_translate("MainWindow", "Название столбца с ссылками"))
        self.scraper_settings.setTabText(self.scraper_settings.indexOf(self.tab_3), _translate("MainWindow", "Excel"))
        self.label_6.setText(_translate("MainWindow", "Число окон:"))
        self.settings.setTabText(self.settings.indexOf(self.Scraper), _translate("MainWindow", "Scraper"))
        self.path_to_parse.setText(_translate("MainWindow", "Файлы html"))
        self.start_parse.setText(_translate("MainWindow", "Start"))
        self.pushButton_top.setText(_translate("MainWindow", "Top"))
        self.elibrary_parse.setText(_translate("MainWindow", "Elibrary"))
        item = self.tableWidget_page.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_page.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Selector"))
        item = self.tableWidget_page.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.tableWidget_page.isSortingEnabled()
        self.tableWidget_page.setSortingEnabled(False)
        self.tableWidget_page.setSortingEnabled(__sortingEnabled)
        self.exel_for_page_load.setText(_translate("MainWindow", "Загрузить excel"))
        self.exel_for_page_save.setText(_translate("MainWindow", "Сохранить как excel"))
        self.parser_settings.setTabText(self.parser_settings.indexOf(self.tab_4), _translate("MainWindow", "Страница"))
        item = self.tableWidget_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Selector_1"))
        item = self.tableWidget_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Selector_2"))
        item = self.tableWidget_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.tableWidget_table.isSortingEnabled()
        self.tableWidget_table.setSortingEnabled(False)
        self.tableWidget_table.setSortingEnabled(__sortingEnabled)
        self.selector_for_table.setText(_translate("MainWindow", "#restab"))
        self.selector_for_table.setPlaceholderText(_translate("MainWindow", "селектор место поиска"))
        self.exel_for_table_load.setText(_translate("MainWindow", "Загрузить excel"))
        self.exel_for_table_save.setText(_translate("MainWindow", "Сохранить как excel"))
        self.parser_settings.setTabText(self.parser_settings.indexOf(self.tab_5), _translate("MainWindow", "Таблица"))
        self.settings.setTabText(self.settings.indexOf(self.Parser), _translate("MainWindow", "Parser"))
        self.save_cookie.setText(_translate("MainWindow", "Save Cookie"))
        self.path_to_proxy.setText(_translate("MainWindow", "Файл proxy"))
        self.set_cookie.setText(_translate("MainWindow", "Выбрать Cookie"))
        self.checkBox_use_cookie.setText(_translate("MainWindow", "Использовать Cookie"))
        self.lineEdit_start_page.setText(_translate("MainWindow", "https://elibrary.ru/"))
        self.label_4.setText(_translate("MainWindow", "Стартовая страница браузера"))
        self.label_5.setText(_translate("MainWindow", "Преписка к ссылкам для парсера"))
        self.lineEdit_link_parse.setText(_translate("MainWindow", "https://elibrary.ru/"))
        self.checkBox_use_proxy.setText(_translate("MainWindow", "Proxy"))
        self.delete_html.setText(_translate("MainWindow", "Удалить html файлы"))
        self.proxy_list_read.setItemText(0, _translate("MainWindow", "По списку"))
        self.proxy_list_read.setItemText(1, _translate("MainWindow", "Случайный"))
        self.settings.setTabText(self.settings.indexOf(self.tab), _translate("MainWindow", "Settings"))
        self.textEdit_history.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))