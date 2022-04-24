#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui


class Insert_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(667, 136,800,100)
        self.setWindowTitle('Добавление новой строки')
        self.Table = Table(self)

        self.btn = QPushButton('Добавить', self)
        self.btn.resize(80, 30)
        self.btn.move(600, 65)
        self.btn.clicked.connect(self.insert_data)

        self.btn = QPushButton('Отмена', self)
        self.btn.resize(80, 30)
        self.btn.move(700, 65)
        self.btn.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

    def insert_data(self):
        pass

class Table(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 765, 50)
        self.setColumnCount(8)
        self.setRowCount(1)
        self.verticalHeader().hide()
        self.setHorizontalHeaderLabels(['id', 'Имя', 'Фамилия', 'Отчество', 'Пол', "Дата рождения",
                                        "Должность", "Отдел"])
        header = self.horizontalHeader()
        header.setDefaultSectionSize(95)



#
# app = QApplication(sys.argv)
# ex = Insert_window()
# ex.show()
# sys.exit(app.exec_())



# здесь идентификатор
#         self.id = QLineEdit(self)
#         self.id.resize(100, 20)
#         self.id.move(500, 60)
#         self.id.setReadOnly(True)
# здесь имя
#         self.name = QLineEdit(self)
#         self.name.resize(150, 40)
#         self.name.move(300, 110)
# здесь фамилия
#         self.familiya = QLineEdit(self)
#         self.familiya.resize(150, 40)
#         self.familiya.move(300, 160)
# здесь отчество
#         self.otchestvo = QLineEdit(self)
#         self.otchestvo.resize(150, 40)
#         self.otchestvo.move(300, 210)
# здесь пол
#         self.sex = QLineEdit(self)
#         self.sex.resize(150, 40)
#         self.sex.move(300, 260)

# добавить таблицу новую строку
#     def insert(self):
#         fio, oce = self.fio.text(), self.oce.text()
#         try:
#             self.cur.execute("insert into student (name, ocenka) values (%s,%s)",(fio,oce))
#         except (Exception) as error:
#             print("Ошибка при добавлении  данных", error)
#         self.upd()