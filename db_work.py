import psycopg2

con = psycopg2.connect(
    database="staff",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432"
)
# Создание соединения
# def create_connection():
#     try:
#         con = psycopg2.connect(
#             database="staff",
#             user="postgres",
#             password="123456",
#             host="127.0.0.1",
#             port="5432"
#         )
#         cursor = con.cursor()
#         # Распечатать сведения о PostgreSQL
#         print("Информация о сервере PostgreSQL")
#         print(con.get_dsn_parameters(), "\n")
#         # Выполнение SQL-запроса
#         cursor.execute("SELECT version();")
#         # Получить результат
#         record = cursor.fetchone()
#         print("Вы подключены к - ", record, "\n")
#     except (Exception) as error:
#         print("Ошибка при работе с PostgreSQL", error)

# Вставка новой строки
def insert_data():
    try:
        cur = con.cursor()
        cur.execute(
          "INSERT INTO persons (id,name,familiya,otchestvo,pol) VALUES (1, 'John', 'ivanov', 'petrovich', 'male')"
        )
        con.commit()
        print("Record inserted successfully")
        con.close()
    except (Exception) as error:
        print("Ошибка при вставке данных", error)

# Извлечение данных
def extract_data():
    try:
        cur = con.cursor()
        cur.execute(
          "SELECT id,name,familiya,otchestvo,pol from persons"
        )
        rows = cur.fetchall()
        print(rows)
        con.close()
    except (Exception) as error:
        print("Ошибка при извлечении данных", error)

#Удаление строки
def delete_data():
    try:
        cur = con.cursor()
        cur.execute("DELETE from persons where id=1;")
        con.commit()
        con.close()
    except (Exception) as error:
        print("Ошибка при удалении данных", error)

