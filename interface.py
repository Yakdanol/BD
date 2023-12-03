from tkinter import *
from tkinter import Canvas, PhotoImage
import customtkinter as ctk
from main import show, connect_with_bd
from PIL import Image, ImageTk
import commands_sql as bd

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Подключение к базе данных
connection = connect_with_bd()

class App(ctk.CTk):
    # общий конструтор класса
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}-0-0")

        # Инициализация состояний
        self.init_states()

        # Инициализация в первом состоянии
        self.show_menu()

        # Добавляем фоновое изображение
        # self.add_background("1.jpg")

    # инициализация всех состояний - фреймов
    def init_states(self):
        # Фрейм - Основное меню
        self.menu_frame = Frame(self)
        self.init_menu_frame()

        # Фрейм - "Каталог автомобилей"
        self.car_catalog_frame = Frame(self)
        self.init_car_catalog_frame()

        # Фрейм - "Двс автомобилей"
        self.dvs_car_frame = Frame(self)
        self.init_dvs_car_frame()

        # Фрейм - "Электрических автомобилей"
        self.electric_car_frame = Frame(self)
        self.init_electric_car_frame()

        # Фрейм - "Гибридных автомобилей"
        self.hybrid_car_frame = Frame(self)
        self.init_hybrid_car_frame()

        # Фрейм - "Цвета"
        self.colours_frame = Frame(self)
        self.init_colours_frame()

        # Фрейм - "Сделки"
        self.deals_frame = Frame(self)
        self.init_deals_frame()

        # Фрейм - "Покупатели"
        self.buyers_frame = Frame(self)
        self.init_buyers_frame()

        # Фрейм - "Опции всех автомобилей"
        self.all_car_options_frame = Frame(self)
        self.init_all_car_options_frame()

        # Фрейм - "Опиции"
        self.options_frame = Frame(self)
        self.init_options_frame()

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(connection))



    # инициализация фрейма - меню
    def init_menu_frame(self):
        # Кнопка "Каталог автомобилей"
        self.car_catalog_button = ctk.CTkButton(
            self.menu_frame, text="Каталог автомобилей", command=self.show_car_catalog
        )
        self.car_catalog_button.grid(row=0, column=0, padx=300, pady=20, sticky="nsew")
        self.car_catalog_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Двс автомобили"
        self.dvs_car_button = ctk.CTkButton(
            self.menu_frame, text="Двс автомобили", command=self.show_dvs_car
        )
        self.dvs_car_button.grid(row=1, column=0, padx=300, pady=20, sticky="nsew")
        self.dvs_car_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Электрические автомобили"
        self.electric_car_button = ctk.CTkButton(
            self.menu_frame, text="Электрические автомобили", command=self.show_electric_car,
        )
        self.electric_car_button.grid(row=2, column=0, padx=300, pady=20, sticky="nsew")
        self.electric_car_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Гибридные автомобили"
        self.hybrid_car_button = ctk.CTkButton(
            self.menu_frame, text="Гибридные автомобили", command=self.show_hybrid_car
        )
        self.hybrid_car_button.grid(row=3, column=0, padx=300, pady=20, sticky="nsew")
        self.hybrid_car_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Цвета автомобилей"
        self.colours_button = ctk.CTkButton(
            self.menu_frame, text="Цвета автомобилей", command=self.show_colours
        )
        self.colours_button.grid(row=4, column=0, padx=300, pady=20, sticky="nsew")
        self.colours_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Сделки"
        self.deals_button = ctk.CTkButton(
            self.menu_frame, text="Сделки", command=self.show_deals
        )
        self.deals_button.grid(row=5, column=0, padx=300, pady=20, sticky="nsew")
        self.deals_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Покупатели"
        self.buyers_button = ctk.CTkButton(
            self.menu_frame, text="Покупатели", command=self.show_buyers
        )
        self.buyers_button.grid(row=6, column=0, padx=300, pady=20, sticky="nsew")
        self.buyers_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Опции всех автомобилей"
        self.all_car_options_button = ctk.CTkButton(
            self.menu_frame, text="Опции всех автомобилей", command=self.show_all_car_options,
        )
        self.all_car_options_button.grid(row=7, column=0, padx=300, pady=20, sticky="nsew")
        self.all_car_options_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Опции"
        self.options_button = ctk.CTkButton(
            self.menu_frame, text="Опции", command=self.show_options
        )
        self.options_button.grid(row=8, column=0, padx=300, pady=20, sticky="nsew")
        self.options_button.configure(width=200, height=40, font=("Arial", 30))


    # инициализация фрейма - Каталог автомобилей
    def init_car_catalog_frame(self):
        # Кнопка "Назад"
        self.back_button_car_catalog = ctk.CTkButton(
            self.car_catalog_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_car_catalog.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_car_catalog.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Двс автомобилей
    def init_dvs_car_frame(self):
        # Кнопка "Назад"
        self.back_button_dvs_car = ctk.CTkButton(
            self.dvs_car_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_dvs_car.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_dvs_car.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Электрических автомобилей
    def init_electric_car_frame(self):
        # Кнопка "Назад"
        self.back_button_electric_car = ctk.CTkButton(
            self.electric_car_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_electric_car.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_electric_car.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Гибридных автомобилей
    def init_hybrid_car_frame(self):
        # Кнопка "Назад"
        self.back_button_hybrid_car = ctk.CTkButton(
            self.hybrid_car_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_hybrid_car.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_hybrid_car.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Цвета автомобилей
    def init_colours_frame(self):
        # Кнопка "Назад"
        self.back_button_colours = ctk.CTkButton(
            self.colours_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_colours.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_colours.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Сделки
    def init_deals_frame(self):
        # Кнопка "Назад"
        self.back_button_deals = ctk.CTkButton(
            self.deals_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_deals.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_deals.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Покупатели
    def init_buyers_frame(self):
        # Кнопка "Назад"
        self.back_button_buyers = ctk.CTkButton(
            self.buyers_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_buyers.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_buyers.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Опции всех автомобилей
    def init_all_car_options_frame(self):
        # Кнопка "Назад"
        self.back_button_all_car_options = ctk.CTkButton(
            self.all_car_options_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_all_car_options.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_all_car_options.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Опции
    def init_options_frame(self):
        # Кнопка "Назад"
        self.back_button_options = ctk.CTkButton(
            self.options_frame, text="Назад",
            command=self.show_menu, fg_color="grey",
        )
        self.back_button_options.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_options.configure(width=200, height=50, font=("Arial", 30))



    # инициализация фрейма - скрытия фреймов
    def hide_all_states(self):
        self.menu_frame.grid_forget()

        self.car_catalog_frame.grid_forget()

        self.dvs_car_frame.grid_forget()

        self.electric_car_frame.grid_forget()

        self.hybrid_car_frame.grid_forget()

        self.colours_frame.grid_forget()

        self.deals_frame.grid_forget()

        self.buyers_frame.grid_forget()

        self.all_car_options_frame.grid_forget()

        self.options_frame.grid_forget()



    # TODO что делает "padx = self.winfo_screenwidth() / 3.7"
    # отображение фрейма - Меню
    def show_menu(self):
        self.hide_all_states()
        self.menu_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 3.13,
            pady=220,
            sticky="nsew",
        )

    # отображение фрейма - Каталог автомобилей
    def show_car_catalog(self):
        self.hide_all_states()
        self.car_catalog_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Двс автомобили
    def show_dvs_car(self):
        self.hide_all_states()
        self.dvs_car_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Электрические автомобили
    def show_electric_car(self):
        self.hide_all_states()
        self.electric_car_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Гибридные автомобили
    def show_hybrid_car(self):
        self.hide_all_states()
        self.hybrid_car_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Цвета
    def show_colours(self):
        self.hide_all_states()
        self.colours_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Сделки
    def show_deals(self):
        self.hide_all_states()
        self.deals_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Покупатели
    def show_buyers(self):
        self.hide_all_states()
        self.buyers_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Опции всех автомобилей
    def show_all_car_options(self):
        self.hide_all_states()
        self.all_car_options_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )

    # отображение фрейма - Опции
    def show_options(self):
        self.hide_all_states()
        self.options_frame.grid(
            row=0, column=0, padx=self.winfo_screenwidth() / 3.7, pady=220, sticky="nsew"
        )



    # добавление фона - надо фиксить потом
    def add_background(self, image_path):
        # # Загрузка изображения с помощью Pillow
        # image = Image.open(image_path)
        #
        # # Преобразование изображения в формат PhotoImage
        # photo = PhotoImage(image)
        #
        # # Создание элемента Canvas
        # canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        # canvas.grid(row=0, column=0, sticky="nsew")
        #
        # # Размещение изображения на Canvas
        # canvas.create_image(0, 0, anchor="nw", image=photo)

        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        canvas = Canvas(
            self, width=self.winfo_screenwidth(), height=self.winfo_screenheight()
        )
        canvas.grid(row=0, column=0, sticky="nsew")
        canvas.create_image(0, 0, anchor="nw", image=photo)

    # закрытие окна и окончание работы с базой
    def on_closing(self, connection):
        connection.close()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()