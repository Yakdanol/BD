from tkinter import *
from tkinter import Canvas, PhotoImage, ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from interface import admin_interface
from client_interface import client_interface
from tkinter import simpledialog, messagebox


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


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
        #self.background_images = {}

    # инициализация всех состояний - фреймов
    def init_states(self):
        # Загружаем фоновое изображение
        self.background_image = ImageTk.PhotoImage(file="1.jpg")

        # Создайте метку (Label) для отображения изображения
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Фрейм - Основное меню
        self.menu_frame = Frame(self)
        self.init_menu_frame()

        # Фрейм - Вход для администратора
        self.login_admin_frame = Frame(self)
        self.init_login_admin_frame()

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())

    # инициализация фрейма - Меню
    def init_menu_frame(self):
        # Кнопка "Клиент"
        self.client_button = ctk.CTkButton(
            self.menu_frame, text="Войти как клиент", command=client_interface
        )
        self.client_button.grid(row=0, column=0, padx=300, pady=20, sticky="nsew")
        self.client_button.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Администратор"
        self.admin_button = ctk.CTkButton(
            self.menu_frame, text="Войти как администратор", command=self.show_login_admin
        )
        self.admin_button.grid(row=1, column=0, padx=300, pady=20, sticky="nsew")
        self.admin_button.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Вход для администратора
    def init_login_admin_frame(self):

        # # Элемент для ввода логина
        # self.temp_login = Entry(self.login_admin_frame, font=("Arial", 14), width=30)
        # # этот объект - поле для ввода, а не параметр, который мы ввели
        # self.temp_login.grid(row=0, column=1, padx=300, pady=25, sticky="nsew")

        # Элемент для ввода логина
        self.temp_login = Entry(self.login_admin_frame, font=("Arial", 20), width=30)
        self.temp_login.grid(row=0, column=0, padx=500, pady=25, sticky="nsew")

        # Элементы для ввода пароля
        self.temp_password = Entry(self.login_admin_frame, font=("Arial", 20), width=30)
        self.temp_password.grid(row=1, column=0, padx=500, pady=25, sticky="nsew")

        # Кнопка "Подтвердить"
        self.confirm_button_login_admin = ctk.CTkButton(self.login_admin_frame, text="Подтвердить",
            command=lambda: self.check_admin_credentials())
        # отправляем в confirm указатель на функцию, НЕ СТРОКУ
        self.confirm_button_login_admin.grid(row=2, column=0, padx=300, pady=25, sticky="nsew")
        self.confirm_button_login_admin.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Назад"
        self.back_button_login_admin = ctk.CTkButton(
            self.login_admin_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_login_admin.grid(row=3, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_login_admin.configure(width=200, height=50, font=("Arial", 30))

    def check_admin_credentials(self):
        username = self.temp_login.get()
        password = self.temp_password.get()

        if username == "1" and password == "1": # postgres, 12345
            # Очистить поля для ввода логина и пароля
            self.temp_login.delete(0, 'end')
            self.temp_password.delete(0, 'end')

            # Скрыть текущее окно
            #self.hide_all_states()
            # Закрыть текущее окно
            # self.quit()
            # self.destroy()

            admin_interface()

        else:
            messagebox.showerror("Ошибка", "Введены неверные данные")
            # Очистить поля для ввода логина и пароля
            self.temp_login.delete(0, 'end')
            self.temp_password.delete(0, 'end')

            app.show_menu()


    # инициализация функции - скрытия фреймов
    def hide_all_states(self):
        self.menu_frame.grid_forget()
        self.login_admin_frame.grid_forget()


    # TODO padx отвечает за сдвиги таблицы с кнопками по горизонтали
    # TODO pady отвечает за сдвиги таблицы с кнопками по вертикали
    # TODO надо бы сделать по центру или оставить так, +- ровно

    # отображение фрейма - Меню
    def show_menu(self):
        self.hide_all_states()
        self.menu_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 3.5,
            pady=500,
            sticky="nsew",
        )
        # Устанавливаем фрейм меню по центру окна
        # frame_x = self.winfo_screenwidth() / 3.7
        # frame_y = self.winfo_screenheight() / 2 - 75  # Высота фрейма меню - 150 (сумма высоты кнопок)
        # self.menu_frame.grid(row=0, column=0, padx=frame_x, pady=frame_y, sticky="nsew")

    def show_login_admin(self):
        self.hide_all_states()
        self.login_admin_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=300,
            sticky="nsew",
        )
        # Устанавливаем фрейм входа для администратора по центру окна
        # frame_x = self.winfo_screenwidth() / 2.5
        # frame_y = self.winfo_screenheight() / 2 - 75  # Высота фрейма входа для админа - 150 (сумма высоты элементов)
        # self.login_admin_frame.grid(row=0, column=0, padx=frame_x, pady=frame_y, sticky="nsew")


    def on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = App_general_menu()
    app.mainloop()