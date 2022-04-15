import psycopg2
from PyQt5.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 150)
w.move(550, 300)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())

# try:
#     con = psycopg2.connect(
#         database="staff_db",
#         user="postgres",
#         password="123456",
#         host="127.0.0.1",
#         port="5432"
#     )
#     cursor = con.cursor()
#     # Распечатать сведения о PostgreSQL
#     print("Информация о сервере PostgreSQL")
#     print(con.get_dsn_parameters(), "\n")
#     # Выполнение SQL-запроса
#     cursor.execute("SELECT version();")
#     # Получить результат
#     record = cursor.fetchone()
#     print("Вы подключены к - ", record, "\n")
# except (Exception) as error:
#     print("Ошибка при работе с PostgreSQL", error)





