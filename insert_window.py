#!/usr/bin/python3

import sys, psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui
con = psycopg2.connect(
    database="staff",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432",
)

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
        data = []
        try:
            for i in range(0, self.Table.columnCount()):
                data.append(self.Table.item(0,i).text())
            data[0] = int(data[0])
        except:
            print('er')
        try:
            cur = con.cursor()
            cur.execute(
        "INSERT INTO persons (id,name,familiya,otchestvo,pol,birthday) VALUES (data[0], 'data[1]', 'data[2]', 'Petrovich','male','2012-11-11');"
        "INSERT INTO positions (id, position_name,id_person) VALUES (2, 'master', 2);"
        "INSERT INTO department (id, department_name, id_person) VALUES (2, 'grs', 2)"
            )
            con.commit()
            print("Record inserted successfully")
            con.close()
        except (Exception) as error:
            print("Ошибка при вставке данных", error)
            data = self.Table.item(0,0).text()
            print(data)

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
        # self.id = QTableWidgetItem('5859')
        # self.setItem(0,0,self.id)




app = QApplication(sys.argv)
ex = Insert_window()
ex.show()
sys.exit(app.exec_())



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