import psycopg2
import random

con = psycopg2.connect(
    database="staff",
    user="postgres",
    password="123456",
    host="127.0.0.1",
    port="5432",
)
name = ['Ярослав', 'Лев', 'Василиса', 'Дарья', 'Виктория', 'Максим', 'Анастасия', 'Анна', 'Сергей', 'Арина', 'Павел',
        'Иван', 'Алексей', 'Максим', 'Таисия', ]
last_name = ['Александров ', 'Алексеев ', 'Анисимова ', 'Антонов ', 'Баранов ', 'Белоусов ', 'Богданова ', 'Богомолов ',
             'Борисова ', 'Булатов ', 'Булгаков ', 'Васильев ', 'Васильева ', 'Глебова ', 'Денисов ', ]
middle_name = ['Данииловна', 'Романович', 'Константинович', 'Германовна', 'Михайлович', 'Тимуровна', 'Николаевич',
               'Александрович', 'Иванович', 'Степанович', 'Матвеевич', 'Ильич', 'Платоновна', 'Данииловна',
               'Павловна', ]
sex = ['мужской', 'женский']
birthday = ['2022-01-13', '2034-06-15', '1959-02-01', '2002-11-04', '1981-02-13', '1931-05-16', '2003-06-02',
            '2031-06-26', '1990-07-09', '2026-11-09', '2029-06-30', '2031-10-27', '2032-09-27', '1993-09-24',
            '1967-09-25', ]
departments = ['Бухгалтерия', 'Отдел кадров', 'Руководство', 'Связь', 'Энергетики', 'Транспортники', 'Мед персонал',
               'КИП', 'Метод кабинет', 'Пожарники', ]
positions = ['Сантехник', 'Машинист', 'Водитель', 'Преподаватель', 'Начальник', 'Доктор', 'Приборист', 'Оператор',
             'Плотник', ]

p = name[random.randint(0,14)]
print(p)
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
                "INSERT INTO persons (id,name,familiya,otchestvo,pol,birthday) VALUES (2, 'Petr', 'Petrov', 'Petrovich',"
                "'male','2012-11-11');"
                " INSERT INTO positions (id, position_name,id_person) VALUES (2, 'master', 2);"
                "INSERT INTO department (id, department_name, id_person) VALUES (2, 'grs', 2)"
            )
        con.commit()
        print("Record inserted successfully")
        con.close()
    except (Exception) as error:
        print("Ошибка при вставке данных", error)


def random_insert():
    try:
        cur = con.cursor()
        for i in range(0,10):
            cur.execute(
                "INSERT INTO persons (id,name,familiya,otchestvo,pol,birthday) VALUES (i, 'name[random.randint(0,14)]', "
                "'last_name[random.randint(0,14)]', 'middle_name[random.randint(0,14)]','sex[random.randint(0,1)]',"
                "'birthday[random.randint(0,14)]');"
                " INSERT INTO positions (id, position_name,id_person) VALUES (i, 'positions[random.randint(0,8)]', i);"
                "INSERT INTO department (id, department_name, id_person) VALUES (i, 'departments[random.randint(0,9)]', i)"
            )
        con.commit()
        print(" Random record inserted successfully")
        con.close()
    except (Exception) as error:
        print("Ошибка при вставке данных", error)



# Извлечение данных
def extract_data():
    try:
        cur = con.cursor()
        cur.execute(
            "SELECT id,name,familiya,otchestvo,pol  from persons"
        )
        rows = cur.fetchall()
        print(rows)
        con.close()
    except (Exception) as error:
        print("Ошибка при извлечении данных", error)


def extract_alldata():
    try:
        cur = con.cursor()
        cur.execute(
            "SELECT persons.*,positions.position_name,department.department_name FROM persons INNER JOIN positions ON persons.id=positions.id_person INNER JOIN department ON persons.id=department.id_person"
        )
        rows = cur.fetchall()
        print(rows)
        con.close()
    except (Exception) as error:
        print("Ошибка при извлечении данных", error)


# Удаление строки
def delete_data():
    try:
        cur = con.cursor()
        cur.execute("DELETE from persons where id=2;")
        con.commit()
        con.close()
    except (Exception) as error:
        print("Ошибка при удалении данных", error)


# extract_data()
# extract_alldata()
# delete_data()
# insert_data()
