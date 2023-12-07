import psycopg2
from psycopg2 import Error
import tkinter.font as tkFont


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

        # Создание объекта шрифта для оценки ширины текста
        font = tkFont.Font(family="Arial", size=22)  # Установите шрифт и размер, соответствующие вашему Treeview

        # Вычисляем максимальную ширину каждого столбца, включая заголовок
        col_widths = {header: font.measure(header) for header in headers}
        for row in rows:
            for i, val in enumerate(row):
                width = font.measure(str(val))
                if width > col_widths[headers[i]]:
                    col_widths[headers[i]] = width

        # Установка заголовков и связывание с функцией сортировки
        self.tree['columns'] = headers
        for header in headers:
            self.tree.heading(header, text=header,
                              command=lambda _col=header: self.treeview_sort_column(self.tree, _col, False))
            self.tree.column(header, anchor='center', width=col_widths[header] + 10)  # Установка ширины столбца

        # Очистка таблицы перед заполнением новыми данными
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Вставка новых данных
        for row in rows:
            self.tree.insert('', 'end', values=row)

    # Возврат количества столбцов
    return len(headers)

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
