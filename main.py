#!/usr/bin/python3

import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit
from PyQt5 import QtGui


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
# подключить базу данных
        self.con()
# параметры окна
        self.setGeometry(100, 100, 500, 600)
        self.setWindowTitle('Список сотрудников')
        self.tb = Tb(self)
# кнопка "обновить"
        self.btn = QPushButton('Обновить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 10)
        self.btn.clicked.connect(self.upd)
# здесь идентификатор
        self.id = QLineEdit(self)
        self.id.resize(150, 40)
        self.id.move(300, 60)
        self.id.setReadOnly(True)
# здесь имя
        self.name = QLineEdit(self)
        self.name.resize(150, 40)
        self.name.move(300, 110)
# здесь фамилия
        self.familiya = QLineEdit(self)
        self.familiya.resize(150, 40)
        self.familiya.move(300, 160)
# здесь отчество
        self.otchestvo = QLineEdit(self)
        self.otchestvo.resize(150, 40)
        self.otchestvo.move(300, 210)
# здесь пол
        self.sex = QLineEdit(self)
        self.sex.resize(150, 40)
        self.sex.move(300, 260)
# кнопка добавить запись
        self.btn = QPushButton('Добавить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 310)
        self.btn.clicked.connect(self.insert)
# кнопка удалить запись
        self.btn = QPushButton('Удалить', self)
        self.btn.resize(150, 40)
        self.btn.move(300, 360)
        self.btn.clicked.connect(self.delete)
# соединение с базой данных
    def con(self):
        self.conn = psycopg2.connect(user = "postgres",
                              password = "123456",
                              host = "localhost",
                              port = "5432",
                              database = "staff_db")
        self.cur = self.conn.cursor()
# обновить таблицу и поля
    def upd(self):
        self.conn.commit()
        self.tb.updt()
        self.id.setText('')
        self.name.setText('')
        self.familiya.setText('')
        self.otchestvo.setText('')
        self.sex.setText('')
# добавить таблицу новую строку
    def insert(self):
        fio, oce = self.fio.text(), self.oce.text()
        try:
            self.cur.execute("insert into student (name, ocenka) values (%s,%s)",(fio,oce))
        except:
            pass
        self.upd()
# удалить из таблицы строку
    def delete(self):
        try:
            ids = int(self.id.text()) # идентификатор строки
        except:
            return
        self.cur.execute("delete from student where id=%s",(ids,))
        self.upd()


class Tb(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 280, 500)
        self.setColumnCount(5)
        self.verticalHeader().hide()
        self.updt() # обновить таблицу
        self.setEditTriggers(QTableWidget.NoEditTriggers) # запретить изменять поля
        self.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице

# обновление таблицы
    def updt(self):
        self.clear()
        self.setRowCount(0)
        self.setHorizontalHeaderLabels(['id', 'Имя', 'Фамилия', 'Отчество', 'Пол']) # заголовки столцов
        self.wg.cur.execute("select * from staff_info order by id")
        rows = self.wg.cur.fetchall()
        i = 0
        for elem in rows:
            self.setRowCount(self.rowCount() + 1)
            j = 0
            for t in elem: # заполняем внутри строки
                self.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1
        self.resizeColumnsToContents()

# обработка щелчка мыши по таблице
    def cellClick(self, row, col): # row - номер строки, col - номер столбца
        self.wg.id.setText(self.item(row, 0).text())
        self.wg.fio.setText(self.item(row, 1).text().strip())
        self.wg.oce.setText(self.item(row, 2).text().strip())


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())





