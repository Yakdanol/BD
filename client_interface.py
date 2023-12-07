from tkinter import *
from tkinter import Canvas, PhotoImage, ttk, messagebox
import customtkinter as ctk
from main import show, connect_client_with_bd
from PIL import Image, ImageTk
import commands_client_sql as bd

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Подключение к базе данных
connection = connect_client_with_bd()


class App_client(ctk.CTk):
    # общий конструтор класса
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
        # self.background_images = {}

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

        # Фрейм - "Сделки"
        self.deals_frame = Frame(self)
        self.init_deals_frame()

        # Фрейм - "Опции всех автомобилей"
        self.all_car_options_frame = Frame(self)
        self.init_all_car_options_frame()

        # Фрейм для результата запросов к бд (результат show)
        self.result_state_frame = Frame(self)
        self.init_result_state_frame()

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

        # Кнопка "Все Цвета автомобилей"
        self.colours_button = ctk.CTkButton(
            self.menu_frame,
            text="Доступные цвета автомобилей",
            command=lambda: self.show_result_state(
                bd.colour_of_car_Select_All, self.menu_frame
            ),
        )
        self.colours_button.grid(row=4, column=0, padx=300, pady=20, sticky="nsew")
        self.colours_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Сделки"
        self.deals_button = ctk.CTkButton(
            self.menu_frame, text="Сделки", command=self.show_deals
        )
        self.deals_button.grid(row=5, column=0, padx=300, pady=20, sticky="nsew")
        self.deals_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Опции всех автомобилей"
        self.all_car_options_button = ctk.CTkButton(
            self.menu_frame,
            text="Посмотреть опции автомобиля",
            command=self.show_all_car_options,
        )
        self.all_car_options_button.grid(
            row=7, column=0, padx=300, pady=20, sticky="nsew"
        )
        self.all_car_options_button.configure(width=200, height=40, font=("Arial", 30))

        # Кнопка "Доступные опции"
        self.options_button = ctk.CTkButton(
            self.menu_frame,
            text="Доступные опции",
            command=lambda: self.show_result_state(
                bd.options_Select_All, self.menu_frame
            ),
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
        self.car_catalog1_button.grid(row=0, column=0, padx=300, pady=25, sticky="nsew")
        self.car_catalog1_button.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Поиска по параметрам"
        self.car_catalog2_button = ctk.CTkButton(
            self.car_catalog_frame,
            text="Поиск по названию и модели",
            command=self.show_find_car_catalog,
        )
        self.car_catalog2_button.grid(row=1, column=0, padx=300, pady=25, sticky="nsew")
        self.car_catalog2_button.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Назад"
        self.back_button_car_catalog = ctk.CTkButton(
            self.car_catalog_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_car_catalog.grid(
            row=2, column=0, padx=300, pady=25, sticky="nsew"
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
        self.dvs_car1_button.grid(row=0, column=0, padx=300, pady=25, sticky="nsew")
        self.dvs_car1_button.configure(width=200, height=50, font=("Arial", 30))

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
        self.electric_car1_button.configure(width=200, height=50, font=("Arial", 30))

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
        self.hybrid_car1_button.grid(row=0, column=0, padx=300, pady=25, sticky="nsew")
        self.hybrid_car1_button.configure(width=200, height=50, font=("Arial", 30))

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
        self.deals1_button.grid(row=0, column=0, padx=300, pady=25, sticky="nsew")
        self.deals1_button.configure(width=200, height=50, font=("Arial", 30))

        # Кнопка "Назад"
        self.back_button_deals = ctk.CTkButton(
            self.deals_frame,
            text="Назад",
            command=self.show_menu,
            fg_color="grey",
        )
        self.back_button_deals.grid(row=6, column=0, padx=300, pady=25, sticky="nsew")
        self.back_button_deals.configure(width=200, height=50, font=("Arial", 30))

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
        self.all_car_options1_button.configure(width=200, height=50, font=("Arial", 30))

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

        self.deals_frame.pack_forget()

        self.all_car_options_frame.pack_forget()

        self.result_state_frame.pack_forget()

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
            padx=(self.winfo_screenwidth() / 3.5), pady=220
        )

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
        self.dvs_car_frame.configure(padx=(self.winfo_screenwidth() / 3), pady=220)

    # отображение фрейма - Электрические автомобили
    def show_electric_car(self):
        self.hide_all_states()
        self.electric_car_frame.pack(fill="both", expand=True)
        self.electric_car_frame.configure(
            padx=(self.winfo_screenwidth() / 3.8), pady=220
        )

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

    # отображение фрейма - Опции всех автомобилей
    def show_all_car_options(self):
        self.hide_all_states()
        self.all_car_options_frame.pack(fill="both", expand=True)
        self.all_car_options_frame.configure(
            padx=(self.winfo_screenwidth() / 3.5), pady=220
        )

    # TODO надо править padx для конкретных окно
    def show_result_state(self, sql_request, current_frame):
        self.previous_frame = current_frame
        self.hide_all_states()
        num_columns = show(self, connection, sql_request)

        padx_value = {
            13: self.winfo_screenwidth() / 6,
            12: self.winfo_screenwidth() / 5.5,
            11: self.winfo_screenwidth() / 5,
            10: self.winfo_screenwidth() / 4.5,
            9: self.winfo_screenwidth() / 3,
            8: self.winfo_screenwidth() / 3.5,
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
        temp = to_save.get().strip().split(" ")
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
            cursor.execute(
                bd.insert_into_crco(num_rows, client_id, emp_id, temp[0], temp[3])
            )
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
    app = App_client()
    app.mainloop()


def client_interface():
    app_client = App_client()
    app_client.mainloop()
