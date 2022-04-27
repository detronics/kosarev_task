#!/usr/bin/python3

import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QTableView
from insert_window import Insert_window,Table
import csv

con = psycopg2.connect(
    database="staff",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432",
)

class ExtractWindow(QWidget):
    def __init__(self,param='prof'):
        super().__init__()
        self.setGeometry(0, 0, 400, 500)
        self.setWindowTitle('Выборка данных')
        self.param = param
        self.Table = ExtractTable(self)
        self.btn = QPushButton('Экспорт в xlsx', self)
        self.btn.resize(80, 35)
        self.btn.move(10, 425)
        self.btn.clicked.connect(self.export)

    def export(self):
        with open(r'C:\test.csv', 'w') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            for row in range(self.Table.rowCount()):
                row_data = []
                for col in range(self.Table.columnCount()):
                    item = self.Table.item(row, col)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)


class ExtractTable(QTableWidget):
    def __init__(self, wg):
        self.wg = wg
        super().__init__(wg)
        self.setGeometry(10, 10, 300, 400)
        self.setColumnCount(2)
        self.verticalHeader().hide()
        self.resizeColumnsToContents()
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.updt()

    def updt(self):
        if self.wg.param == 'prof':
            self.setHorizontalHeaderLabels(['Название должности', 'Количество персонала'])
        else:
            self.setHorizontalHeaderLabels(['Название отдела', 'Количество персонала'])
        cur = con.cursor()
        if self.wg.param == 'prof':
            cur.execute("SELECT position_name, COUNT(position_name) FROM positions GROUP BY position_name")
        else:
            cur.execute("SELECT department_name, COUNT(department_name) FROM department GROUP BY department_name")
        rows = cur.fetchall()
        i = 0
        for elem in rows:
            self.setRowCount(self.rowCount() + 1)
            j = 0
            for t in elem: # заполняем внутри строки
                self.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        self.resizeColumnsToContents()


