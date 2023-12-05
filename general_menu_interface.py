from tkinter import *
from tkinter import Canvas, PhotoImage, ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import commands_sql as bd
from main import show, connect_client_with_bd
from interface import admin_interface
from client_interface import client_interface
from tkinter import simpledialog, messagebox


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Подключение к базе данных
#connection = connect_client_with_bd()


class App_general_menu(ctk.CTk):
    # общий конструтор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}-0-0")

        # Инициализация состояний
        self.init_states()

        # Инициализация в первом состоянии
        self.show_menu()

        # Словарь для хранения фоновых изображений
        self.background_images = {}

    # инициализация всех состояний - фреймов
    def init_states(self):
        # # Загружаем фоновое изображение
        # self.background_image = ImageTk.PhotoImage(file="1.jpg")
        #
        # # Создайте метку (Label) для отображения изображения
        # self.background_label = Label(self, image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Фрейм - Основное меню
        self.menu_frame = Frame(self)
        self.init_menu_frame()

        # Фрейм для четвертого состояния (результат show)
        self.result_state_frame = Frame(self)
        self.init_result_state_frame()

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

    # инициализация фрейма - Меню
    def init_menu_frame(self):
        # Кнопка "Клиент"
        self.client_button = ctk.CTkButton(
            self.menu_frame, text="Войти как клиент", command=client_interface
        )
        self.client_button.grid(row=0, column=0, padx=300, pady=20, sticky="nsew")
        self.client_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Администратор"
        self.admin_button = ctk.CTkButton(
            self.menu_frame, text="Войти как администратор", command=self.check_admin_credentials
        )
        self.admin_button.grid(row=1, column=0, padx=300, pady=20, sticky="nsew")
        self.admin_button.configure(width=200, height=40, font=("Arial", 30))

        self.username_entry = Entry(self.menu_frame, font=("Arial", 14), width=30)
        self.password_entry = Entry(self.menu_frame, font=("Arial", 14), show='*', width=30)
        self.login_button = ctk.CTkButton(
            self.menu_frame, text="Войти", command=self.check_admin_credentials
        )

    # инициализация фрейма - Вход для администратора
    def init_login_admin_frame(self):
        # Кнопка "Входа"
        self.client_button = ctk.CTkButton(
            self.menu_frame, text="", command=client_interface
        )
        self.client_button.grid(row=0, column=0, padx=300, pady=20, sticky="nsew")
        self.client_button.configure(width=200, height=40, font=("Arial", 30))


    def toggle_admin_login(self):
        self.username_entry.grid(row=2, column=0, padx=300, pady=10, sticky="nsew")
        self.password_entry.grid(row=3, column=0, padx=300, pady=10, sticky="nsew")
        self.login_button.grid(row=4, column=0, padx=300, pady=20, sticky="nsew")

    def check_admin_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":  # Замените эти значения на свои
            admin_interface()
        else:
            ctk.show_error("Ошибка", "Введены неверные данные")

    def init_result_state_frame(self):
        # Создайте объект стиля
        style = ttk.Style()

        # Настройте стиль "Treeview"
        style.configure("Treeview", font=("Arial", 16))  # Измените шрифт и размер текста
        style.configure("Treeview.Heading", font=("Arial", 18, "bold"))  # Измените шрифт и размер заголовков столбцов

        # Настройте высоту строк в стиле "Treeview"
        style.configure("Treeview", rowheight=40)

        # Treeview для отображения данных в виде таблицы
        self.tree = ttk.Treeview(self.result_state_frame, style="Treeview")
        self.tree.grid(row=0, column=0, padx=(10, 10), pady=(25, 0), sticky="nsew")

        # Создаем виджеты Scrollbar
        self.vertical_scrollbar = Scrollbar(
            self.result_state_frame, orient="vertical", command=self.tree.yview
        )
        self.vertical_scrollbar.grid(row=0, column=1, sticky="ns")

        self.horizontal_scrollbar = Scrollbar(
            self.result_state_frame, orient="horizontal", command=self.tree.xview
        )
        self.horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

        # Привязываем Scrollbar к Treeview
        self.tree.configure(
            yscrollcommand=self.vertical_scrollbar.set,
            xscrollcommand=self.horizontal_scrollbar.set,
        )

        # Ограничиваем размеры Treeview
        self.tree.config(height=25, show="headings")

        # Кнопка "Назад"
        self.back_button_result = ctk.CTkButton(
            self.result_state_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_result.grid(
            row=2, column=0, padx=(10, 10), pady=(0, 50), sticky="nsew"
        )
        # self.back_button_result.place(connection=10, y=675)  # Задайте нужные вам координаты кнопки


    # инициализация функции - скрытия фреймов
    def hide_all_states(self):
        self.menu_frame.grid_forget()


    # TODO padx отвечает за сдвиги таблицы с кнопками по горизонтали
    # TODO pady отвечает за сдвиги таблицы с кнопками по вертикали
    # TODO надо бы сделать по центру или оставить так, +- ровно

    # отображение фрейма - Меню
    def show_menu(self):
        self.hide_all_states()
        self.menu_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 3.7,
            pady=100,
            sticky="nsew",
        )

    def check_admin_credentials(self):
        username = simpledialog.askstring("Логин", "Введите логин:")
        password = simpledialog.askstring("Пароль", "Введите пароль:", show='*')

        if username == "admin" and password == "password":  # Замените эти значения на свои
            admin_interface()
        else:
            self.show_error_and_return_to_menu()

    def show_error_and_return_to_menu(self):
        messagebox.showerror("Ошибка", "Введены неверные данные")
        app.show_menu()

    # закрытие окна и окончание работы с базой
    # def on_closing(self, connection):
    #     connection.close()
    #     self.destroy()

    def on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = App_general_menu()
    app.mainloop()