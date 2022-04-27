#!/usr/bin/python3

import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QTableView
from PyQt5.QtSql import QSqlDatabase
from insert_window import Insert_window,Table
import pandas
# from main import MyWidget.param
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
        print('init')
        self.setGeometry(0, 0, 400, 500)
        self.setWindowTitle('Выборка данных')
        self.param = param
        self.lol = 2
        self.Table = ExtractTable(self)
        self.btn = QPushButton('Экспорт в xlsx', self)
        self.btn.resize(80, 35)
        self.btn.move(10, 425)
        self.btn.clicked.connect(self.export)

    def export(self):
        print(self.param)
        columnHeaders = []
        for j in range(self.Table.model().columnCount()):
            columnHeaders.append(self.Table.horizontalHeaderItem(j).text())
        df = pandas.DataFrame(columns=columnHeaders)
        for row in range(self.Table.rowCount()):
            for col in range(self.Table.columnCount()):
                df.at[row, columnHeaders[col]] = self.Table.item(row, col).text()
        # df.to_excel(r'D:\Dummy File XYZ.xlsx', index=False)
        print('Excel file exported')

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


# app = QApplication(sys.argv)
# ex = ExtractWindow()
# ex.show()
# sys.exit(app.exec_())