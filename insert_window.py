#!/usr/bin/python3

import sys, psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit


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
        self.setGeometry(667, 136, 800, 100)
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
                data.append(self.Table.item(0, i).text())
        except:
            print('error')
        try:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO persons (id,name,familiya,otchestvo,pol,birthday) VALUES (%s,%s,%s,%s,%s,%s)",
                (data[0], data[1], data[2], data[3], data[4], data[5]))
            cur.execute(
                "INSERT INTO positions (id, position_name,id_person) VALUES (%s,%s,%s)",
                (data[0], data[6], data[0]))
            cur.execute(
                "INSERT INTO department (id, department_name, id_person) VALUES (%s,%s,%s)",
                (data[0], data[7], data[0]))
            con.commit()
            print("Record inserted successfully")
            con.close()
        except (Exception) as error:
            print("Ошибка при вставке данных", error)
        self.close()



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


