from tkinter import *
from tkinter import Canvas, PhotoImage, ttk, messagebox
import customtkinter as ctk
from main import show, connect_admin_with_bd
from PIL import Image, ImageTk
import commands_admin_sql as bd

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Подключение к базе данных
connection = connect_admin_with_bd()

key_column_names = ["id_car", "id_colour", "id_deal", "id_buyer", "id_number", "id_option"]
my_width = 200
my_height = 50
my_pady = 25
my_font = "Arial"

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

        # храним предыдущий фрейм для кнопки назад
        self.previous_frame = None

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

        # Фрейм - "Поиск автомобиля в Каталоге автомобилей"
        self.find_car_catalog_frame = Frame(self)
        self.init_find_car_catalog_frame()

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

        # Фреймы для добавления в бд
        self.insert_car_frame = Frame(self)
        self.init_insert_car_frame()

        self.insert_dvs_frame = Frame(self)
        self.init_insert_dvs_frame()

        self.insert_electric_frame = Frame(self)
        self.init_insert_electric_frame()

        self.insert_hybrid_frame = Frame(self)
        self.init_insert_hybrid_frame()

        self.insert_colour_frame = Frame(self)
        self.init_insert_colour_frame()

        self.insert_deals_frame = Frame(self)
        self.init_insert_deals_frame()

        self.insert_buyers_frame = Frame(self)
        self.init_insert_buyers_frame()

        self.insert_general_options_frame = Frame(self)
        self.init_insert_general_options_frame()

        self.insert_options_frame = Frame(self)
        self.init_insert_options_frame()

        self.remove_car_frame = Frame(self)
        self.init_remove_car_frame()

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(connection))

    # инициализация фрейма - Меню
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
            self.menu_frame,
            text="Электрические автомобили",
            command=self.show_electric_car,
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
            self.menu_frame,
            text="Опции всех автомобилей",
            command=self.show_all_car_options,
        )
        self.all_car_options_button.grid(
            row=7, column=0, padx=300, pady=20, sticky="nsew"
        )
        self.all_car_options_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Опции"
        self.options_button = ctk.CTkButton(
            self.menu_frame, text="Опции", command=self.show_options
        )
        self.options_button.grid(row=8, column=0, padx=300, pady=20, sticky="nsew")
        self.options_button.configure(width=200, height=40, font=("Arial", 30))

    # инициализация фрейма - Каталог автомобилей
    def init_car_catalog_frame(self):
        # Кнопка "Все автомобили"
        self.car_catalog1_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Все автомобили",
            command=lambda: self.show_result_state(
                bd.car_catalog_Select_All, self.car_catalog_frame
            ),
        )
        self.car_catalog1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.car_catalog1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Добавить автомобиль"
        self.car_catalog2_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Добавить автомобиль",
            command=lambda: self.show_insert_menu("car_catalog"),
        )
        self.car_catalog2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.car_catalog2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Поиска по параметрам"
        self.car_catalog2_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Поиск по названию и модели",
            command=self.show_find_car_catalog,
        )
        self.car_catalog2_button.grid(row=2, column=0, padx=300, pady=25, sticky="nsew")
        self.car_catalog2_button.configure(width=200, height=50, font=("Arial", 30))

        self.car_catalog3_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Удалить автомобиль",  # удалить двигатель
            command=lambda: self.show_remove_menu("car_catalog"),
        )
        self.car_catalog3_button.grid(row=3, column=0, padx=300, pady=25, sticky="nsew")
        self.car_catalog3_button.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Назад"
        self.back_button_car_catalog = ctk.CTkButton(
            self.car_catalog_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_car_catalog.grid(
            row=4, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_car_catalog.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - поиска автомобилей в Каталоге автомобилей
    def init_find_car_catalog_frame(self):
        # Поля для ввода бренда
        self.entry_brand = ctk.CTkEntry(
            self.find_car_catalog_frame, placeholder_text="Введите бренд автомобиля"
        )
        self.entry_brand.grid(row=0, column=0, padx=300, pady=25, sticky="nsew")
        self.entry_brand.configure(width=400, height=50, font=("Arial", 30))

        self.entry_model = ctk.CTkEntry(
            self.find_car_catalog_frame, placeholder_text="Введите марку автомобиля"
        )
        self.entry_model.grid(row=1, column=0, padx=300, pady=25, sticky="nsew")
        self.entry_model.configure(width=400, height=50, font=("Arial", 30))

        # Кнопка выполнения поиска
        self.find_car_catalog_button = ctk.CTkButton(
            self.find_car_catalog_frame,
            text="Поиск",
            command=lambda: self.find_car_catalog(),
        )
        self.find_car_catalog_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        self.find_car_catalog_button.configure(width=200, font=("Arial", 30))

        # Кнопка "Назад"
        self.back_button_find_car_catalog = ctk.CTkButton(
            self.find_car_catalog_frame,
            text="Назад",
            command=self.show_car_catalog,
            fg_color="grey",
        )
        self.back_button_find_car_catalog.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.back_button_find_car_catalog.configure(width=150, font=("Arial", 20))

    def find_car_catalog(self):
        # Получите значения из полей ввода бренда и модели автомобиля
        brand = self.entry_brand.get().strip()
        model = self.entry_model.get().strip()

        if not brand and not model:
            messagebox.showerror("Ошибка", "Вы ничего не ввели!")
            # Очистить поля для ввода логина и пароля
            self.entry_brand.delete(0, "end")
            self.entry_model.delete(0, "end")

        else:
            # Формирование SQL запроса в зависимости от введенных данных
            if not model:
                sql_request = bd.find_car_catalog_brand(brand)
            elif not brand:
                sql_request = bd.find_car_catalog_model(model)
            else:
                sql_request = bd.find_car_catalog_brand_and_model(brand, model)

            # Вызов нового метода для выполнения и проверки SQL запроса
            if self.execute_and_check_sql(sql_request):
                self.show_result_state(sql_request, self.find_car_catalog_frame)
            else:
                messagebox.showinfo("Информация", "Таких автомобилей нет в Каталоге!")
                self.entry_brand.delete(0, "end")
                self.entry_model.delete(0, "end")

    # инициализация фрейма - Двс автомобилей
    def init_dvs_car_frame(self):
        # Кнопка "Все автомобили"
        self.dvs_car1_button = ctk.CTkButton(
            self.dvs_car_frame,
            text="Все Двс автомобили",
            command=lambda: self.show_result_state(
                bd.dvs_car_Select_All, self.dvs_car_frame
            ),
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
        self.back_button_dvs_car.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Электрических автомобилей
    def init_electric_car_frame(self):
        # Кнопка "Все Электрические автомобили"
        self.electric_car1_button = ctk.CTkButton(
            self.electric_car_frame,
            text="Все Электрические автомобили",
            command=lambda: self.show_result_state(
                bd.electric_car_Select_All, self.electric_car_frame
            ),
        )
        self.electric_car1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.electric_car1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # self.electric_car2_button = ctk.CTkButton(
        #     self.electric_car_frame,
        #     text="Добавить электромобиль",
        #     command=lambda: self.show_insert_menu("electric"),
        # )
        # self.electric_car2_button.grid(
        #     row=1, column=0, padx=300, pady=25, sticky="nsew"
        # )
        # self.electric_car2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

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
            width=200, height=50, font=("Arial", 30)
        )

    # инициализация фрейма - Гибридных автомобилей
    def init_hybrid_car_frame(self):
        # Кнопка "Все Гибридные автомобили"
        self.hybrid_car1_button = ctk.CTkButton(
            self.hybrid_car_frame,
            text="Все Гибридные автомобили",
            command=lambda: self.show_result_state(
                bd.hybrid_car_Select_All, self.hybrid_car_frame
            ),
        )
        self.hybrid_car1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.hybrid_car1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # self.hybrid_car2_button = ctk.CTkButton(
        #     self.hybrid_car_frame,
        #     text="Добавить гибрид",
        #     command=lambda: self.show_insert_menu("hybrid"),
        # )
        # self.hybrid_car2_button.grid(
        #     row=1, column=0, padx=300, pady=25, sticky="nsew"
        # )
        # self.hybrid_car2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

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
        self.back_button_hybrid_car.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Цвета автомобилей
    def init_colours_frame(self):
        # Кнопка "Все Цвета автомобилей"
        self.colours1_button = ctk.CTkButton(
            self.colours_frame,
            text="Все Цвета автомобилей",
            command=lambda: self.show_result_state(
                bd.colour_of_car_Select_All, self.colours_frame
            ),
        )
        self.colours1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.colours1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        self.colours2_button = ctk.CTkButton(
            self.colours_frame,
            text="Добавить цвет",
            command=lambda: self.show_insert_menu("colour"),
        )
        self.colours2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.colours2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_colours = ctk.CTkButton(
            self.colours_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_colours.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_colours.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Сделки
    def init_deals_frame(self):
        # Кнопка "Все Сделки"
        self.deals1_button = ctk.CTkButton(
            self.deals_frame,
            text="Все Сделки",
            command=lambda: self.show_result_state(
                bd.deals_Select_All, self.deals_frame
            ),
        )
        self.deals1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.deals1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        self.deals2_button = ctk.CTkButton(
            self.deals_frame,
            text="Добавить сделку",
            command=lambda: self.show_insert_menu("deals"),
        )
        self.deals2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.deals2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_deals = ctk.CTkButton(
            self.deals_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_deals.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_deals.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Покупатели
    def init_buyers_frame(self):
        # Кнопка "Все Покупатели"
        self.buyers1_button = ctk.CTkButton(
            self.buyers_frame,
            text="Все Покупатели",
            command=lambda: self.show_result_state(
                bd.buyers_Select_All, self.buyers_frame
            ),
        )
        self.buyers1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.buyers1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        self.buyers2_button = ctk.CTkButton(
            self.buyers_frame,
            text="Добавить покупателя",
            command=lambda: self.show_insert_menu("buyers"),
        )
        self.buyers2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.buyers2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_buyers = ctk.CTkButton(
            self.buyers_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_buyers.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_buyers.configure(width=200, height=50, font=("Arial", 30))

    # инициализация фрейма - Опции всех автомобилей
    def init_all_car_options_frame(self):
        # Кнопка "Опции всех автомобилей"
        self.all_car_options1_button = ctk.CTkButton(
            self.all_car_options_frame,
            text="Опции всех автомобилей",
            command=lambda: self.show_result_state(
                bd.all_car_options_Select_All, self.all_car_options_frame
            ),
        )
        self.all_car_options1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.all_car_options1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        self.all_car_options2_button = ctk.CTkButton(
            self.all_car_options_frame,
            text="Добавить опцию автомобилю",
            command=lambda: self.show_insert_menu("general_options"),
        )
        self.all_car_options2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.all_car_options2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

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
            width=200, height=50, font=("Arial", 30)
        )

    # инициализация фрейма - Опции
    def init_options_frame(self):
        # Кнопка "Доступные опции"
        self.options1_button = ctk.CTkButton(
            self.options_frame,
            text="Доступные опции",
            command=lambda: self.show_result_state(
                bd.options_Select_All, self.options_frame
            ),
        )
        self.options1_button.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.options1_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        self.options2_button = ctk.CTkButton(
            self.options_frame,
            text="Добавить опцию",
            command=lambda: self.show_insert_menu("options"),
        )
        self.options2_button.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.options2_button.configure(width=my_width, height=my_height, font=(my_font, 30))

        # Кнопка "Назад"
        self.back_button_options = ctk.CTkButton(
            self.options_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_options.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_options.configure(width=200, height=50, font=("Arial", 30))

    def init_result_state_frame(self):
        # Создайте объект стиля
        style = ttk.Style()

        # Настройте стиль "Treeview"
        style.configure(
            "Treeview", font=("Arial", 16)
        )  # Измените шрифт и размер текста
        style.configure(
            "Treeview.Heading", font=("Arial", 18, "bold")
        )  # Измените шрифт и размер заголовков столбцов

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
            command=self.go_back,
            fg_color="grey",
        )
        self.back_button_result.grid(
            row=2, column=0, padx=(10, 10), pady=(0, 50), sticky="nsew"
        )

        # Привязка события выбора строки
        self.tree.bind("<<TreeviewSelect>>", self.on_car_selected)

        # self.back_button_result.place(connection=10, y=675)
        # Задайте нужные вам координаты кнопки

    def init_insert_car_frame(self):
        # Поля для ввода данных об автомобиле
        self.entry_idcar = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="ID автомобиля"
        )
        self.entry_idcar.grid(
            row=0, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_idcar.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_brand = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Марка автомобиля"
        )
        self.entry_brand.grid(
            row=1, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_brand.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_model = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Модель автомобиля"
        )
        self.entry_model.grid(
            row=2, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_model.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_year = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Дата выпуска (ГГГГ-ММ-ДД)"
        )
        self.entry_year.grid(
            row=3, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_year.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_colour = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Номер цвета"
        )
        self.entry_colour.grid(
            row=4, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_colour.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_price = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Цена"
        )
        self.entry_price.grid(
            row=5, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_price.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_type = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Тип (DVS, Hybrid, Electric)"
        )
        self.entry_type.grid(
            row=6, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_type.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_condition = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Состояние (New, Used)"
        )
        self.entry_condition.grid(
            row=7, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_condition.configure(width=my_width, height=40, font=(my_font, 14))

        self.entry_range = ctk.CTkEntry(
            self.insert_car_frame,
            placeholder_text="Запас хода"
        )
        self.entry_range.grid(
            row=8, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_range.configure(width=my_width, height=40, font=(my_font, 14))

        self.button_insert_car = ctk.CTkButton(
            self.insert_car_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("car_catalog"),
        )
        self.button_insert_car.grid(
            row=9, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.button_insert_car.configure(width=my_width, height=40, font=(my_font, 20))

        self.back_button_insert_car = ctk.CTkButton(
            self.insert_car_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_car.grid(
            row=10, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.back_button_insert_car.configure(width=my_width, height=40, font=(my_font, 20))

    def init_insert_dvs_frame(self):
        # Поля для ввода данных

        self.entry_power = ctk.CTkEntry(
            self.insert_dvs_frame,
            placeholder_text="Мощность"
        )
        self.entry_power.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_power.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_capacity = ctk.CTkEntry(
            self.insert_dvs_frame,
            placeholder_text="Объем"
        )
        self.entry_capacity.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_capacity.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_fuel = ctk.CTkEntry(
            self.insert_dvs_frame,
            placeholder_text="Вид топлива (1, 2, 3)"
        )
        self.entry_fuel.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_fuel.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_class = ctk.CTkEntry(
            self.insert_dvs_frame,
            placeholder_text="Экологический класс"
        )
        self.entry_class.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_class.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_dvs = ctk.CTkButton(
            self.insert_dvs_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("dvs_car"),
        )
        self.button_insert_dvs.grid(
            row=4, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_dvs.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_electric_frame(self):
        # Поля для ввода данных

        self.entry_power_electric = ctk.CTkEntry(
            self.insert_electric_frame,
            placeholder_text="Мощность"
        )
        self.entry_power_electric.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_power_electric.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_capacity_battery = ctk.CTkEntry(
            self.insert_electric_frame,
            placeholder_text="Объем батареи"
        )
        self.entry_capacity_battery.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_capacity_battery.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_electric = ctk.CTkButton(
            self.insert_electric_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("electric_car"),
        )
        self.button_insert_electric.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_electric.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_hybrid_frame(self):

        self.entry_power_hybrid = ctk.CTkEntry(
            self.insert_hybrid_frame,
            placeholder_text="Мощность"
        )
        self.entry_power_hybrid.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_power_hybrid.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_capacity_hybrid = ctk.CTkEntry(
            self.insert_hybrid_frame,
            placeholder_text="Объем двигателя"
        )
        self.entry_capacity_hybrid.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_capacity_hybrid.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_class_hybrid = ctk.CTkEntry(
            self.insert_hybrid_frame,
            placeholder_text="Экологический класс"
        )
        self.entry_class_hybrid.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_class_hybrid.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_power_electric_hybrid = ctk.CTkEntry(
            self.insert_hybrid_frame,
            placeholder_text="Мощность электродвигателя"
        )
        self.entry_power_electric_hybrid.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_power_electric_hybrid.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_capacity_battery_hybrid = ctk.CTkEntry(
            self.insert_hybrid_frame,
            placeholder_text="Объем батареи"
        )
        self.entry_capacity_battery_hybrid.grid(
            row=4, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_capacity_battery_hybrid.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_hybrid = ctk.CTkButton(
            self.insert_hybrid_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("hybrid_car"),
        )
        self.button_insert_hybrid.grid(
            row=5, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_hybrid.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_colour_frame(self):
        self.entry_id_colour = ctk.CTkEntry(
            self.insert_colour_frame,
            placeholder_text="ID цвета"
        )
        self.entry_id_colour.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_id_colour.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_colour_name = ctk.CTkEntry(
            self.insert_colour_frame,
            placeholder_text="Цвет"
        )
        self.entry_colour_name.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_colour_name.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_colour = ctk.CTkButton(
            self.insert_colour_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("colour_of_car"),
        )
        self.button_insert_colour.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_colour.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_colour = ctk.CTkButton(
            self.insert_colour_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_colour.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_colour.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_deals_frame(self):
        self.entry_id_deals = ctk.CTkEntry(
            self.insert_deals_frame,
            placeholder_text="ID сделки"
        )
        self.entry_id_deals.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_id_deals.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_idcar_deals = ctk.CTkEntry(
            self.insert_deals_frame,
            placeholder_text="ID автомобиля"
        )
        self.entry_idcar_deals.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_idcar_deals.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_idbuyer_deals = ctk.CTkEntry(
            self.insert_deals_frame,
            placeholder_text="ID покупателя"
        )
        self.entry_idbuyer_deals.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_idbuyer_deals.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_date_deals = ctk.CTkEntry(
            self.insert_deals_frame,
            placeholder_text="Дата продажи (ГГГГ-ММ-ДД)"
        )
        self.entry_date_deals.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_date_deals.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_price_deals = ctk.CTkEntry(
            self.insert_deals_frame,
            placeholder_text="Цена продажи"
        )
        self.entry_price_deals.grid(
            row=4, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_price_deals.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_deals = ctk.CTkButton(
            self.insert_deals_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("deals"),
        )
        self.button_insert_deals.grid(
            row=5, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_deals.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_deals = ctk.CTkButton(
            self.insert_deals_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_deals.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_deals.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_buyers_frame(self):
        self.entry_id_buyers = ctk.CTkEntry(
            self.insert_buyers_frame,
            placeholder_text="ID покупателя"
        )
        self.entry_id_buyers.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_id_buyers.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_name_buyers = ctk.CTkEntry(
            self.insert_buyers_frame,
            placeholder_text="Имя Фамилия"
        )
        self.entry_name_buyers.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_name_buyers.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_contacts_buyers = ctk.CTkEntry(
            self.insert_buyers_frame,
            placeholder_text="Контакт"
        )
        self.entry_contacts_buyers.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_contacts_buyers.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_buyers = ctk.CTkButton(
            self.insert_buyers_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("buyers"),
        )
        self.button_insert_buyers.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_buyers.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_buyers = ctk.CTkButton(
            self.insert_buyers_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_buyers.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_buyers.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_general_options_frame(self):
        self.entry_id_general = ctk.CTkEntry(
            self.insert_general_options_frame,
            placeholder_text="ID связи"
        )
        self.entry_id_general.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_id_general.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_idcar_general = ctk.CTkEntry(
            self.insert_general_options_frame,
            placeholder_text="ID автомобиля"
        )
        self.entry_idcar_general.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_idcar_general.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_idoption_general = ctk.CTkEntry(
            self.insert_general_options_frame,
            placeholder_text="ID опции"
        )
        self.entry_idoption_general.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_idoption_general.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_general = ctk.CTkButton(
            self.insert_general_options_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("general_car_options"),
        )
        self.button_insert_general.grid(
            row=3, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_general.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_general = ctk.CTkButton(
            self.insert_general_options_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_general.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_general.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_insert_options_frame(self):
        self.entry_id_option = ctk.CTkEntry(
            self.insert_options_frame,
            placeholder_text="ID опции"
        )
        self.entry_id_option.grid(
            row=0, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_id_option.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.entry_description_option = ctk.CTkEntry(
            self.insert_options_frame,
            placeholder_text="Описание опции"
        )
        self.entry_description_option.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.entry_description_option.configure(width=my_width, height=my_height, font=(my_font, 14))

        self.button_insert_options = ctk.CTkButton(
            self.insert_options_frame,
            text="Добавить",
            command=lambda: self.make_insert_to_db("options"),
        )
        self.button_insert_options.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_insert_options.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.back_button_insert_options = ctk.CTkButton(
            self.insert_options_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_insert_options.grid(
            row=10, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.back_button_insert_options.configure(width=my_width, height=my_height, font=(my_font, 20))

    def init_remove_car_frame(self):
        self.entry_remove_id_car = ctk.CTkEntry(
            self.remove_car_frame,
            placeholder_text="ID автомобиля"
        )
        self.entry_remove_id_car.grid(
            row=0, column=0, padx=300, pady=15, sticky="nsew"
        )
        self.entry_remove_id_car.configure(width=my_width, height=40, font=(my_font, 14))

        self.button_remove_car = ctk.CTkButton(
            self.remove_car_frame,
            text="Удалить",
            command=lambda: self.remove_from_db("car_catalog"),
        )
        self.button_remove_car.grid(
            row=1, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_remove_car.configure(width=my_width, height=my_height, font=(my_font, 20))

        self.button_remove_car_back = ctk.CTkButton(
            self.remove_car_frame,
            text="Назад",
            command=self.show_car_catalog,
            fg_color="grey"
        )
        self.button_remove_car_back.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
        )
        self.button_remove_car_back.configure(width=my_width, height=my_height, font=(my_font, 20))

    # Метод для обработки выбора строки в Treeview
    def on_car_selected(self, event):
        if (
            self.previous_frame == self.car_catalog_frame
            or self.previous_frame == self.dvs_car_frame
            or self.previous_frame == self.electric_car_frame
            or self.previous_frame == self.hybrid_car_frame
        ):
            selection = self.tree.selection()
            if selection:
                selected_item = selection[0]
                car_data = self.tree.item(selected_item, "values")
                car_id = car_data[0]  # Обязательно, чтобы ID автомобиля находится в первом столбце

                # Запрос к базе данных для получения опций автомобиля
                self.show_result_state(bd.options_select_car(car_id), self.previous_frame)
        else:
            pass

    # Метод для возврата к предыдущему фрейму
    def go_back(self):
        if self.previous_frame:
            self.result_state_frame.pack_forget()  # Скрываем текущий фрейм
            self.previous_frame.pack(
                fill="both", expand=True, pady=25
            )  # Отображаем предыдущий фрейм

    def execute_and_check_sql(self, sql_request):
        with connection.cursor() as cursor:
            cursor.execute(sql_request)
            rows = cursor.fetchall()

        # Проверка на наличие результатов
        if rows:
            return rows
        else:
            return None



    # инициализация функции - скрытия фреймов
    def hide_all_states(self):
        self.menu_frame.pack_forget()

        self.car_catalog_frame.pack_forget()

        self.find_car_catalog_frame.pack_forget()

        self.dvs_car_frame.pack_forget()

        self.electric_car_frame.pack_forget()

        self.hybrid_car_frame.pack_forget()

        self.colours_frame.pack_forget()

        self.deals_frame.pack_forget()

        self.buyers_frame.pack_forget()

        self.all_car_options_frame.pack_forget()

        self.options_frame.pack_forget()

        self.result_state_frame.pack_forget()

        self.insert_car_frame.pack_forget()

        self.insert_dvs_frame.pack_forget()

        self.insert_electric_frame.pack_forget()

        self.insert_hybrid_frame.pack_forget()

        self.insert_colour_frame.pack_forget()

        self.insert_deals_frame.pack_forget()

        self.insert_buyers_frame.pack_forget()

        self.insert_general_options_frame.pack_forget()

        self.insert_options_frame.pack_forget()

        self.remove_car_frame.pack_forget()

    # TODO padx отвечает за сдвиги таблицы с кнопками по горизонтали
    # TODO pady отвечает за сдвиги таблицы с кнопками по вертикали
    # TODO надо бы сделать по центру или оставить так, +- ровно

    # отображение фрейма - Меню
    def show_menu(self):
        self.hide_all_states()
        self.menu_frame.pack(fill="both", expand=True)
        self.menu_frame.configure(padx=(self.winfo_screenwidth() / 3.5), pady=100)

    # отображение фрейма - Каталог автомобилей
    def show_car_catalog(self):
        self.hide_all_states()
        self.car_catalog_frame.pack(fill="both", expand=True)
        self.car_catalog_frame.configure(
            padx=(self.winfo_screenwidth() / 3), pady=220
        )

    # Отображение фрейма - Поиск в Каталоге автомобилей
    def show_find_car_catalog(self):
        self.hide_all_states()
        self.find_car_catalog_frame.pack(fill="both", expand=True)
        self.find_car_catalog_frame.configure(
            padx=(self.winfo_screenwidth() / 3.5), pady=220
        )

    # отображение фрейма - Двс автомобили
    def show_dvs_car(self):
        self.hide_all_states()
        self.dvs_car_frame.pack(fill="both", expand=True)
        self.dvs_car_frame.configure(
            padx=(self.winfo_screenwidth() / 3), pady=220)

    # отображение фрейма - Электрические автомобили
    def show_electric_car(self):
        self.hide_all_states()
        self.electric_car_frame.pack(fill="both", expand=True)
        self.electric_car_frame.configure(
            padx=(self.winfo_screenwidth() / 3.8), pady=220)

    # отображение фрейма - Гибридные автомобили
    def show_hybrid_car(self):
        self.hide_all_states()
        self.hybrid_car_frame.pack(fill="both", expand=True)
        self.hybrid_car_frame.configure(
            padx=(self.winfo_screenwidth() / 3.8), pady=220)

    # отображение фрейма - Цвета
    def show_colours(self):
        self.hide_all_states()
        self.colours_frame.pack(fill="both", expand=True)
        self.colours_frame.configure(
            padx=(self.winfo_screenwidth() / 3), pady=220)

    # отображение фрейма - Сделки
    def show_deals(self):
        self.hide_all_states()
        self.deals_frame.pack(fill="both", expand=True)
        self.deals_frame.configure(
            padx=(self.winfo_screenwidth() / 2.5), pady=220)

    # отображение фрейма - Покупатели
    def show_buyers(self):
        self.hide_all_states()
        self.buyers_frame.pack(fill="both", expand=True)
        self.buyers_frame.configure(
            padx=(self.winfo_screenwidth() / 2.5), pady=220)

    # отображение фрейма - Опции всех автомобилей
    def show_all_car_options(self):
        self.hide_all_states()
        self.all_car_options_frame.pack(fill="both", expand=True)
        self.all_car_options_frame.configure(
            padx=(self.winfo_screenwidth() / 3.5), pady=220
        )

    # отображение фрейма - Опции
    def show_options(self):
        self.hide_all_states()
        self.options_frame.pack(fill="both", expand=True)
        self.options_frame.configure(
            padx=(self.winfo_screenwidth() / 2.5), pady=220
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

    # TODO надо править padx для конкретных окно
    def show_result_state(self, sql_request, current_frame):
        self.previous_frame = current_frame
        self.hide_all_states()
        num_columns = show(self, connection, sql_request)

        padx_value = {
            13: self.winfo_screenwidth() / 6,
            12: self.winfo_screenwidth() / 5.5,
            11: self.winfo_screenwidth() / 5,
            10: self.winfo_screenwidth() / 3,
            9: self.winfo_screenwidth() / 2.8,
            8: self.winfo_screenwidth() / 2,
            7: self.winfo_screenwidth() / 2,
            6: self.winfo_screenwidth() / 2.2,
            5: self.winfo_screenwidth() / 2.0,
            4: self.winfo_screenwidth() / 1.8,
            3: self.winfo_screenwidth() / 1.6,
            2: self.winfo_screenwidth() / 1.4,
            1: self.winfo_screenwidth() / 1.3,
            "default": self.winfo_screenwidth() / 4,
        }.get(num_columns, "default")

        self.result_state_frame.pack(
            fill="both",
            expand=True,
            padx=padx_value,
            pady=100,
        )

        # Очистка Treeview перед новыми данными
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Вызов функции show с передачей self в качестве первого аргумента
        show(self, connection, sql_request)

    # отображение фрйема встаки в таблицы
    def show_insert_menu(self, table: str):
        self.hide_all_states()
        if table == "car_catalog":
            self.insert_car_frame.pack(fill="both", expand=True)
            self.insert_car_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=50)
        elif table == "dvs":
            self.insert_dvs_frame.pack(fill="both", expand=True)
            self.insert_dvs_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "electric":
            self.insert_electric_frame.pack(fill="both", expand=True)
            self.insert_electric_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "hybrid":
            self.insert_hybrid_frame.pack(fill="both", expand=True)
            self.insert_hybrid_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "colour":
            self.insert_colour_frame.pack(fill="both", expand=True)
            self.insert_colour_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "deals":
            self.insert_deals_frame.pack(fill="both", expand=True)
            self.insert_deals_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "buyers":
            self.insert_buyers_frame.pack(fill="both", expand=True)
            self.insert_buyers_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "general_options":
            self.insert_general_options_frame.pack(fill="both", expand=True)
            self.insert_general_options_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)
        elif table == "options":
            self.insert_options_frame.pack(fill="both", expand=True)
            self.insert_options_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=220)

    def show_remove_menu(self, table: str):
        self.hide_all_states()
        if table == "car_catalog":
            self.remove_car_frame.pack(fill="both", expand=True)
            self.remove_car_frame.configure(
                padx=(self.winfo_screenwidth() / 2.5), pady=50)

    # Проверка вхождения перед вставкой
    def record_exists(self, cursor, table_name, key_column, key_value):
        # Проверка существования записи с определенным ключом
        if key_value == "":
            return True
        select_query = f"SELECT 1 FROM {table_name} WHERE {key_column} = %s"
        cursor.execute(select_query, (key_value,))
        return cursor.fetchone() is not None

    def record_exists2(self, cursor, table_name, key_column, key_value):
        # Проверка существования записи с определенным ключом
        if key_value == "":
            return False
        select_query = f"SELECT 1 FROM {table_name} WHERE {key_column} = %s"
        cursor.execute(select_query, (key_value,))
        return cursor.fetchone() is not None

    # Вставка в таблицы
    def make_insert_to_db(self, table):
        sql_request = bd.insert_into_table + " " + table + " VALUES "
        data = []
        idx = -1
        if table == "car_catalog":
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

            idx = 0
            sql_request += f"({data[0]}, '{data[1]}', '{data[2]}', '{data[3]}', {data[4]}, {data[5]}, '{data[6]}', '{data[7]}', {data[8]})"
        elif table == "dvs_car":
            data = [
                self.entry_power.get(),
                self.entry_capacity.get(),
                self.entry_fuel.get(),
                self.entry_class.get()
            ]
            idx = 0
            sql_request += f"({self.entry_idcar.get()}, {data[0]}, {data[1]}, {data[2]}, '{data[3]}', 'DVS')"
        elif table == "electric_car":
            data = [
                self.entry_power_electric.get(),
                self.entry_capacity_battery.get()
            ]
            idx = 0
            sql_request += f"({self.entry_idcar.get()}, {data[0]}, {data[1]}, 'Electric')"
        elif table == "hybrid_car":
            data = [
                self.entry_power_hybrid.get(),
                self.entry_capacity_hybrid.get(),
                self.entry_class_hybrid.get(),
                self.entry_power_electric_hybrid.get(),
                self.entry_capacity_battery_hybrid.get()
            ]
            idx = 0
            sql_request += f"({self.entry_idcar.get()}, {data[0]}, {data[1]}, '{data[2]}', {data[3]}, {data[4]}, 'Hybrid')"
        elif table == "colour_of_car":
            data = [
                self.entry_id_colour.get(),
                self.entry_colour_name.get()
            ]
            idx = 1
            sql_request += f"({data[0]}, '{data[1]}')"
        elif table == "deals":
            data = [
                self.entry_id_deals.get(),
                self.entry_idcar_deals.get(),
                self.entry_idbuyer_deals.get(),
                self.entry_date_deals.get(),
                self.entry_price_deals.get()
            ]
            idx = 2
            sql_request += f"({data[0]}, {data[1]}, {data[2]}, '{data[3]}', {data[4]})"
        elif table == "buyers":
            data = [
                self.entry_id_buyers.get(),
                self.entry_name_buyers.get(),
                self.entry_contacts_buyers.get()
            ]
            idx = 3
            sql_request += f"({data[0]}, '{data[1]}', '{data[2]}')"
        elif table == "general_car_options":
            data = [
                self.entry_id_general.get(),
                self.entry_idcar_general.get(),
                self.entry_idoption_general.get()
            ]
            idx = 4
            sql_request += f"({data[0]}, {data[1]}, {data[2]})"
        elif table == "options":
            data = [
                self.entry_id_option.get(),
                self.entry_description_option.get()
            ]
            idx = 5
            sql_request += f"({data[0]}, '{data[1]}')"

        with connection.cursor() as cursor:
            flag = True
            if self.record_exists(cursor, table, key_column_names[idx], data[0]):
                flag = False
            if len(data) == 0:
                flag = False
            for i in range(len(data)):
                if len(data[i]) == 0:
                    flag = False
                    break
            if flag == True:
                cursor.execute(sql_request)
                connection.commit()
                if table == "car_catalog":
                    if data[6] == "DVS":
                        self.show_insert_menu("dvs")
                    elif data[6] == "Electric":
                        self.show_insert_menu("electric")
                    elif data[6] == "Hybrid":
                        self.show_insert_menu("hybrid")
                elif table == "dvs_car":
                    self.show_menu()
                elif table == "electric_car":
                    self.show_menu()
                elif table == "hybrid_car":
                    self.show_menu()

                messagebox.showinfo("Успешно", "Данные добавлены в таблицу")
            else:
                messagebox.showerror("Ошибка", "Неверные данные или ключ уже существует!")

    def remove_from_db(self, table):
        data = ["id_car", self.entry_remove_id_car.get()]
        remove_car_query = bd.delete_from_table(table, data)

        flag = True
        if data[1] == "":
            flag = False
        if self.record_exists2(connection.cursor(), "deals", "id_car", data[1]):
            flag = False
        if not self.record_exists2(connection.cursor(), "car_catalog", "id_car", data[1]):
            flag = False

        if flag == True:
            with connection.cursor() as cursor:
                while self.record_exists2(cursor, "general_car_options", "id_car", data[1]):
                    remove_options_query = bd.delete_from_table("general_car_options", data)
                    cursor.execute(remove_options_query)
                    connection.commit()

                get_type_query = f"SELECT car_type FROM car_catalog WHERE id_car = {data[1]}"
                cursor.execute(get_type_query)
                car_type = cursor.fetchone()[0]
                if car_type == "DVS":
                    remove_dvs_query = bd.delete_from_table("dvs_car", data)
                    cursor.execute(remove_dvs_query)
                    connection.commit()
                elif car_type == "Electric":
                    remove_electric_query = bd.delete_from_table("electric_car", data)
                    cursor.execute(remove_electric_query)
                    connection.commit()
                elif car_type == "Hybrid":
                    remove_hybrid_query = bd.delete_from_table("hybrid_car", data)
                    cursor.execute(remove_hybrid_query)
                    connection.commit()

                cursor.execute(remove_car_query)
                connection.commit()

            messagebox.showinfo("Успешно", "Автомобиль удален")
            self.entry_remove_id_car.delete(0, "end")

        else:
            messagebox.showerror("Ошибка", "Невозможно удалить автомобиль\nНеверный ID или Автомобиль участвует в сделке")
            self.entry_remove_id_car.delete(0, "end")


    # Сортировка данных в Treeview при клике на заголовок столбца
    def treeview_sort_column(self, tree, col, reverse):
        # Преобразование данных к числам, если это возможно
        try:
            l = [
                (int(tree.set(k, col)), k)
                if tree.set(k, col).isdigit()
                else (tree.set(k, col), k)
                for k in tree.get_children("")
            ]
        # Если преобразование в число не удается, обработать как строку
        except ValueError:
            l = [(tree.set(k, col), k) for k in tree.get_children("")]
        l.sort(reverse=reverse)

        # Переставлять элементы в отсортированном порядке
        for index, (val, k) in enumerate(l):
            tree.move(k, "", index)

        # Изменение направления сортировки для следующего клика
        tree.heading(
            col, command=lambda: self.treeview_sort_column(tree, col, not reverse)
        )


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

def admin_interface():
    app_admin = App()
    app_admin.mainloop()