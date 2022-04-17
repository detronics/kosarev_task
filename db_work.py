import psycopg2

def create_connection():
    try:
        con = psycopg2.connect(
            database="staff_db",
            user="postgres",
            password="123456",
            host="127.0.0.1",
            port="5432"
        )
        cursor = con.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(con.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")
    except (Exception) as error:
        print("Ошибка при работе с PostgreSQL", error)