#!/usr/bin/python3

import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QTableView
from PyQt5.QtSql import QSqlDatabase
from insert_window import Insert_window,Table


class ExtractWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(667, 136, 800, 100)
        self.setWindowTitle('Добавление новой строки')
        self.Table = ExtractTable(self)


class ExtractTable(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 700, 400)
        self.setColumnCount(2)
        self.verticalHeader().hide()
        self.setEditTriggers(QTableWidget.NoEditTriggers) # запретить изменять поля
