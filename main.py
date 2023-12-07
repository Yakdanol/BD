import psycopg2
from psycopg2 import Error


# Подключение к базе данных
def connect_admin_with_bd():
    connection = psycopg2.connect(
        user="postgres",
        password="Flikster999",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )

    return connection

# Подключение к базе данных
def connect_client_with_bd():
    connection = psycopg2.connect(
        user="client",
        password="client",
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

        # Установка заголовков и связывание с функцией сортировки
        self.tree['columns'] = headers
        for header in headers:
            self.tree.heading(header, text=header,
                              command=lambda _col=header: self.treeview_sort_column(self.tree, _col, False))
            self.tree.column(header, anchor='center')  # Выравнивание по центру

        # Очистка таблицы перед заполнением новыми данными
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Вставка новых данных
        for row in rows:
            self.tree.insert('', 'end', values=row)

    # Возврат количества столбцов
    return len(headers)

def make_insert_to_db(self, connection, sql_request: str, data: list):
    #TODO: не добавляет данные в таблицу
    #TODO: разделить на каждую таблицу
    with connection.cursor() as cursor:
        flag = True
        for i in range(len(data)):
            if len(data[i]) == 0:
                flag = False
                break
        if flag == True:
            cursor.execute(sql_request)
            print(sql_request)

if __name__ == "__main__":
    try:
        connection = connect_admin_with_bd()
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
