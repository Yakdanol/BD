import psycopg2
from psycopg2 import Error


# Подключение к базе данных
def connect_with_bd():
    connection = psycopg2.connect(
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )

    return connection

def show():
    print()


if __name__ == "__main__":
    try:
        connection = connect_with_bd()
        cursor = connection.cursor()

        cursor.execute("SELECT * from car_catalog")
        record = cursor.fetchall()
        print("Результат", record)

    except (Exception, Error) as error:
        print("\nОшибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("\nСоединение с PostgreSQL закрыто")
