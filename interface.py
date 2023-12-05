from tkinter import *
from tkinter import Canvas, PhotoImage, ttk
import customtkinter as ctk
from main import show, connect_with_bd
from PIL import Image, ImageTk
import commands_sql as bd

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Подключение к базе данных
connection = connect_with_bd()

my_width = 200
my_height = 20
my_pady = 20
my_font = "xo oriel"

class App(ctk.CTk):
    # общий конструктор класса
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
        # #
        # # Создайте метку (Label) для отображения изображения
        # self.background_label = Label(self, image=self.background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

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

        # Фрейм для четвертого состояния (результат show)
        self.result_state_frame = Frame(self)
        self.init_result_state_frame()

        self.insert_car_frame = Frame(self)
        self.init_insert_car_frame()

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(connection))

    # инициализация фрейма - Меню
    def init_menu_frame(self):
        # Кнопка "Каталог автомобилей"
        self.car_catalog_button = ctk.CTkButton(
            self.menu_frame, text="Каталог автомобилей", command=self.show_car_catalog
        )
        self.car_catalog_button.grid(row=0, column=0, padx=300, pady=20, sticky="nsew")
        self.car_catalog_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Двс автомобили"
        self.dvs_car_button = ctk.CTkButton(
            self.menu_frame, text="Двс автомобили", command=self.show_dvs_car
        )
        self.dvs_car_button.grid(row=1, column=0, padx=300, pady=20, sticky="nsew")
        self.dvs_car_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Электрические автомобили"
        self.electric_car_button = ctk.CTkButton(
            self.menu_frame,
            text="Электрические автомобили",
            command=self.show_electric_car,
        )
        self.electric_car_button.grid(row=2, column=0, padx=300, pady=20, sticky="nsew")
        self.electric_car_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Гибридные автомобили"
        self.hybrid_car_button = ctk.CTkButton(
            self.menu_frame, text="Гибридные автомобили", command=self.show_hybrid_car
        )
        self.hybrid_car_button.grid(row=3, column=0, padx=300, pady=20, sticky="nsew")
        self.hybrid_car_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Цвета автомобилей"
        self.colours_button = ctk.CTkButton(
            self.menu_frame, text="Цвета автомобилей", command=self.show_colours
        )
        self.colours_button.grid(row=4, column=0, padx=300, pady=20, sticky="nsew")
        self.colours_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Сделки"
        self.deals_button = ctk.CTkButton(
            self.menu_frame, text="Сделки", command=self.show_deals
        )
        self.deals_button.grid(row=5, column=0, padx=300, pady=20, sticky="nsew")
        self.deals_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Покупатели"
        self.buyers_button = ctk.CTkButton(
            self.menu_frame, text="Покупатели", command=self.show_buyers
        )
        self.buyers_button.grid(row=6, column=0, padx=300, pady=20, sticky="nsew")
        self.buyers_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Опции всех автомобилей"
        self.all_car_options_button = ctk.CTkButton(
            self.menu_frame,
            text="Опции всех автомобилей",
            command=self.show_all_car_options,
        )
        self.all_car_options_button.grid(
            row=7, column=0, padx=300, pady=20, sticky="nsew"
        )
        self.all_car_options_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Опции"
        self.options_button = ctk.CTkButton(
            self.menu_frame, text="Опции", command=self.show_options
        )
        self.options_button.grid(row=8, column=0, padx=300, pady=20, sticky="nsew")
        self.options_button.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Каталог автомобилей
    def init_car_catalog_frame(self):
        # Кнопка "Все автомобили"
        self.car_catalog1_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Все автомобили",
            command=lambda: self.show_result_state(bd.car_catalog_Select_All),
        )
        self.car_catalog1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.car_catalog1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Добавить автомобиль"
        self.car_catalog2_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Добавить автомобиль",
            command=lambda: self.show_insert_menu(bd.car_catalog_Select_All),
        )
        self.car_catalog2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.car_catalog2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_car_catalog = ctk.CTkButton(
            self.car_catalog_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_car_catalog.grid(
            row=6, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_car_catalog.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Двс автомобилей
    def init_dvs_car_frame(self):
        # Кнопка "Все автомобили"
        self.dvs_car1_button = ctk.CTkButton(
            self.dvs_car_frame,
            text="Все Двс автомобили",
            command=lambda: self.show_result_state(bd.dvs_car_Select_All),
        )
        self.dvs_car1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.dvs_car1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_dvs_car = ctk.CTkButton(
            self.dvs_car_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_dvs_car.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_dvs_car.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Электрических автомобилей
    def init_electric_car_frame(self):
        # Кнопка "Все Электрические автомобили"
        self.electric_car1_button = ctk.CTkButton(
            self.electric_car_frame,
            text="Все Электрические автомобили",
            command=lambda: self.show_result_state(bd.electric_car_Select_All),
        )
        self.electric_car1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.electric_car1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_electric_car = ctk.CTkButton(
            self.electric_car_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_electric_car.grid(
            row=6, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_electric_car.configure(
            width=my_width, height=my_height, font=(my_font, 30)
        )

    # инициализация фрейма - Гибридных автомобилей
    def init_hybrid_car_frame(self):
        # Кнопка "Все Гибридные автомобили"
        self.hybrid_car1_button = ctk.CTkButton(
            self.hybrid_car_frame,
            text="Все Гибридные автомобили",
            command=lambda: self.show_result_state(bd.hybrid_car_Select_All),
        )
        self.hybrid_car1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.hybrid_car1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_hybrid_car = ctk.CTkButton(
            self.hybrid_car_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_hybrid_car.grid(
            row=6, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_hybrid_car.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Цвета автомобилей
    def init_colours_frame(self):
        # Кнопка "Все Цвета автомобилей"
        self.colours1_button = ctk.CTkButton(
            self.colours_frame,
            text="Все Цвета автомобилей",
            command=lambda: self.show_result_state(bd.colour_of_car_Select_All),
        )
        self.colours1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.colours1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_colours = ctk.CTkButton(
            self.colours_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_colours.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_colours.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Сделки
    def init_deals_frame(self):
        # Кнопка "Все Сделки"
        self.deals1_button = ctk.CTkButton(
            self.deals_frame,
            text="Все Сделки",
            command=lambda: self.show_result_state(bd.deals_Select_All),
        )
        self.deals1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.deals1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_deals = ctk.CTkButton(
            self.deals_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_deals.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_deals.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Покупатели
    def init_buyers_frame(self):
        # Кнопка "Все Покупатели"
        self.buyers1_button = ctk.CTkButton(
            self.buyers_frame,
            text="Все Покупатели",
            command=lambda: self.show_result_state(bd.buyers_Select_All),
        )
        self.buyers1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.buyers1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_buyers = ctk.CTkButton(
            self.buyers_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_buyers.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_buyers.configure(width=my_width, height=my_height, font=(my_font, 30))

    # инициализация фрейма - Опции всех автомобилей
    def init_all_car_options_frame(self):
        # Кнопка "Опции всех автомобилей"
        self.all_car_options1_button = ctk.CTkButton(
            self.all_car_options_frame,
            text="Опции всех автомобилей",
            command=lambda: self.show_result_state(bd.all_car_options_Select_All),
        )
        self.all_car_options1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.all_car_options1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_all_car_options = ctk.CTkButton(
            self.all_car_options_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_all_car_options.grid(
            row=6, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_all_car_options.configure(
            width=my_width, height=my_height, font=(my_font, 30)
        )

    # инициализация фрейма - Опции
    def init_options_frame(self):
        # Кнопка "Доступные опции"
        self.options1_button = ctk.CTkButton(
            self.options_frame,
            text="Доступные опции",
            command=lambda: self.show_result_state(bd.options_Select_All),
        )
        self.options1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.options1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_options = ctk.CTkButton(
            self.options_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_options.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_options.configure(width=my_width, height=my_height, font=(my_font, 30))

    def init_result_state_frame(self):
        # Создайте объект стиля
        style = ttk.Style()

        # Настройте стиль "Treeview"
        style.configure("Treeview", font=(my_font, 14))  # Измените шрифт и размер текста
        style.configure("Treeview.Heading", font=(my_font, 16, "bold"))  # Измените шрифт и размер заголовков столбцов

        # Настройте высоту строк в стиле "Treeview"
        style.configure("Treeview", rowheight=30)

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

    def init_insert_car_frame(self):
        # Поля для ввода данных об автомобиле
        self.entry_idcar = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="ID автомобиля"
        )
        self.entry_idcar.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_idcar.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_brand = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Марка автомобиля"
        )
        self.entry_brand.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_brand.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_model = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Модель автомобиля"
        )
        self.entry_model.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_model.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_year = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Дата выпуска (ГГГГ-ММ-ДД)"
        )
        self.entry_year.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_year.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_colour = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Номер цвета"
        )
        self.entry_colour.grid(
            row=4, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_colour.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_price = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Цена"
        )
        self.entry_price.grid(
            row=5, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_price.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_type = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Тип (DVS, Hybrid, Electric)"
        )
        self.entry_type.grid(
            row=6, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_type.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_condition = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Состояние (New, Used)"
        )
        self.entry_condition.grid(
            row=7, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_condition.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_range = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Запас хода"
        )
        self.entry_range.grid(
            row=8, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_range.configure(width=my_width, height=my_height, font=(my_font, 14))

        data = [
            self.entry_idcar.get(),
            self.entry_brand.get(),
            self.entry_model.get(),
            self.entry_year.get(),
            self.entry_colour.get(),
            self.entry_price.get(),
            self.entry_type.get(),
            self.entry_condition.get(),
            self.entry_range.get()
        ]

        query = bd.insert_into_table + " car_catalog VALUES " + f"({data[0]}, '{data[1]}', '{data[2]}', {data[3]}, {data[4]}, {data[5]}, '{data[6]}, '{data[7]}', {data[8]})"
        self.button_insert_car = ctk.CTkButton(
            self.insert_car_frame,
            text="Добавить",
            command=self.make_insert_to_db(query),
        )
        self.button_insert_car.grid(
            row=9, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_car.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_car = ctk.CTkButton(
            self.insert_car_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_car.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_car.configure(width=my_width, height=my_height, font=(my_font, 20))


    # инициализация функции - скрытия фреймов
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

        self.result_state_frame.grid_forget()

        self.insert_car_frame.grid_forget()


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
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Каталог автомобилей
    def show_car_catalog(self):
        self.hide_all_states()
        self.car_catalog_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Двс автомобили
    def show_dvs_car(self):
        self.hide_all_states()
        self.dvs_car_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Электрические автомобили
    def show_electric_car(self):
        self.hide_all_states()
        self.electric_car_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Гибридные автомобили
    def show_hybrid_car(self):
        self.hide_all_states()
        self.hybrid_car_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Цвета
    def show_colours(self):
        self.hide_all_states()
        self.colours_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Сделки
    def show_deals(self):
        self.hide_all_states()
        self.deals_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Покупатели
    def show_buyers(self):
        self.hide_all_states()
        self.buyers_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Опции всех автомобилей
    def show_all_car_options(self):
        self.hide_all_states()
        self.all_car_options_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # отображение фрейма - Опции
    def show_options(self):
        self.hide_all_states()
        self.options_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    # пока не используется
    def get_id(self, func, to_save):
        # фигня какая то, мб поставить заглушку
        temp = to_save.get().strip()
        # print("get_client_id", to_save.get().strip())
        if not temp:
            return
        self.find_id(func(temp))

    # пока не используется
    def create_contract(self, to_save, client_id, emp_id):
        temp = to_save.get().strip().split(' ')
        if not temp:
            return
        self.hide_all_states()
        with connection.cursor() as cursor:
            num_rows = int(cursor.execute(bd.credit_contracts_first))
        with connection.cursor() as cursor:
            cursor.execute(bd.insert_into_cs(num_rows))
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(bd.insert_into_cv(num_rows, temp[0], temp[1], temp[2]))
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(bd.insert_into_clcr(num_rows, client_id))
            connection.commit()
        with connection.cursor() as cursor:
            cursor.execute(bd.insert_into_crco(num_rows, client_id, emp_id, temp[0], temp[3]))
            connection.commit()
        self.hide_all_states()
        self.show_menu()
    
    def confirm_temp(self, func, to_save):
        temp = to_save.get().strip()
        if not temp:
            return
        self.hide_all_states()
        s = func(temp)
        self.show_result_state(s)

    def show_result_state(self, sql_request):
        self.hide_all_states()
        num_columns = show(self, connection, sql_request)
        if num_columns > 7:
            self.result_state_frame.grid(
                row=0,
                column=0,
                padx=self.winfo_screenwidth() / 20,
                pady=my_pady,
                sticky="nsew",
            )
        elif num_columns == 7:
            self.result_state_frame.grid(
                row=0,
                column=0,
                padx=self.winfo_screenwidth() / 8,
                pady=my_pady,
                sticky="nsew",
            )
        elif num_columns == 6:
            self.result_state_frame.grid(
                row=0,
                column=0,
                padx=self.winfo_screenwidth() / 6,
                pady=my_pady,
                sticky="nsew",
            )
        else:
            self.result_state_frame.grid(
                row=0,
                column=0,
                padx=self.winfo_screenwidth() / 3.7,
                pady=my_pady,
                sticky="nsew",
            )

        # Очистка Treeview перед новыми данными
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Вызов функции show с передачей self в качестве первого аргумента
        show(self, connection, sql_request)

    def show_insert_menu(self, table):
        self.hide_all_states()
        # TODO: добавить условия для запроса
        self.insert_car_frame.grid(
            row=0,
            column=0,
            padx=self.winfo_screenwidth() / 2.5,
            pady=my_pady,
            sticky="nsew",
        )

    def make_insert_to_db(self, sql_request: str):
        #TODO: исправить ошибку на компиляции
        with connection.cursor() as cursor:
            cursor.execute(sql_request)

    @staticmethod
    def find_id(sql_request: str):
        with connection.cursor() as cursor:
            cursor.execute(sql_request)
            rows = cursor.fetchall()
            return list(rows[0].values())[0]

    # закрытие окна и окончание работы с базой
    def on_closing(self, connection):
        connection.close()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()