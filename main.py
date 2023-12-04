import psycopg2
from psycopg2 import Error


# Подключение к базе данных
def connect_with_bd():
    connection = psycopg2.connect(
        user="postgres",
        password="Flikster999",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )

    return connection

def show(self, connection, sql_request: str):
    with connection.cursor() as cursor:
        cursor.execute(sql_request)
        rows = cursor.fetchall()
        # Определение заголовков
        headers = [desc[0] for desc in cursor.description]
        # Установка заголовков в Treeview
        self.tree['columns'] = headers
        for header in headers:
            self.tree.heading(header, text=header)
            self.tree.column(header, anchor='center')  # Выравнивание по центру

        # Вставка новых данных в Treeview
        for row in rows:
            self.tree.insert('', 'end', values=tuple(row.values()))

    # Return the number of columns
    return len(headers)

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
