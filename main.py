#!/usr/bin/python3

import sys
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QTableView
from PyQt5.QtSql import QSqlDatabase
from insert_window import Insert_window,Table

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
# подключить базу данных
        self.con()
# параметры окна
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Список сотрудников')
        self.tb = Tb(self)
        self.insert_w = Insert_window()
        self.number = 0
# кнопка "обновить"
        self.btn = QPushButton('Обновить', self)
        self.btn.resize(130, 35)
        self.btn.move(10, 425)
        self.btn.clicked.connect(self.upd)
# кнопка добавить запись
        self.btn = QPushButton('Добавить', self)
        self.btn.resize(130, 35)
        self.btn.move(150, 425)
        self.btn.clicked.connect(self.add)
# кнопка удалить запись
        self.btn = QPushButton('Удалить', self)
        self.btn.resize(130, 35)
        self.btn.move(290, 425)
        self.btn.clicked.connect(self.delete)
# кнопка печать выборки
        self.btn = QPushButton('Печать', self)
        self.btn.resize(130, 35)
        self.btn.move(430, 425)
        self.btn.clicked.connect(self.print)
# кнопка записи изменений строки в БД
        self.btn = QPushButton('Сохранить', self)
        self.btn.resize(130, 35)
        self.btn.move(590, 425)
        self.btn.clicked.connect(self.edit)
# соединение с базой данных
    def con(self):
        self.conn = psycopg2.connect(user = "postgres",
                                    password = "123456",
                                    host = "localhost",
                                    port = "5432",
                                    database = "staff")
        self.cur = self.conn.cursor()

# обновить таблицу
    def upd(self):
        # self.conn.commit()
        self.tb.updt()

# удалить из таблицы строку
    def delete(self):
        num = self.tb.item(self.number, 0).text()
        try:
            self.cur.execute("DELETE FROM persons WHERE id={0}".format(num))
            self.conn.commit()
            self.upd()
        except (Exception) as error:
            print("Ошибка при удалении  данных", error)

# вызов окна печати
    def print(self):
        pass

# вызов добавления новой строки
    def add(self):
        self.insert_w.show()
        self.upd()

# редактирование  строки
    def edit(self):
        row_data=[]
        try:
            for i in range(0, self.tb.columnCount()):
                row_data.append(self.tb.item(self.number, i).text())
        except:
                print('error')
        print(row_data)
        try:
            self.cur.execute(
                "UPDATE  persons SET name=%s,familiya=%s,otchestvo=%s,pol=%s,birthday=%s WHERE id=%s",
                (row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], row_data[0]))
            self.cur.execute(
                "UPDATE positions SET position_name=%s WHERE id_person=%s",
                ( row_data[6],row_data[0]))
            self.cur.execute(
                "UPDATE department SET department_name=%s WHERE id_person=%s",
                (row_data[7], row_data[0]))
            self.conn.commit()
            self.upd()
            print("Record rewrite successfully")
        except (Exception) as error:
            print("Ошибка при перезаписи данных", error)



class Tb(QTableWidget):
    def __init__(self, wg):
        self.wg = wg  # запомнить окно, в котором эта таблица показывается
        super().__init__(wg)
        self.setGeometry(10, 10, 600, 400)
        self.setColumnCount(8)
        self.verticalHeader().hide()
        self.updt() # обновить таблицу
        self.setEditTriggers(QTableWidget.DoubleClicked) # запретить изменять поля
        self.cellClicked.connect(self.cellClick)  # установить обработчик щелча мыши в таблице
        # self.mod = QTableView()
        # self.mod.setModel()
# обновление таблицы
    def updt(self):
        self.clear()
        self.setRowCount(0)
        self.setHorizontalHeaderLabels(['id', 'Имя', 'Фамилия', 'Отчество', 'Пол', "Дата рождения", "Должность","Отдел"]) # заголовки столцов
        self.wg.cur.execute("SELECT persons.*,positions.position_name,department.department_name"
                             " FROM persons INNER JOIN positions ON persons.id=positions.id_person"
                             " INNER JOIN department ON persons.id=department.id_person")
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
        self.wg.number = self.currentIndex().row()



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())





