class Store:
    def __init__(self, name, address, description, phone, working_hours):
        self.name = name
        self.address = address
        self.description = description  # Описание магазина
        self.phone = phone  # Контактный телефон
        self.working_hours = working_hours  # Часы работы
        self.items = {}  # Инициализация пустого словаря для товаров

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price} в магазин '{self.name}'.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price} в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def display_info(self):
        """Выводит информацию о магазине."""
        print(f"Магазин: {self.name}")
        print(f"Адрес: {self.address}")
        print(f"Описание: {self.description}")
        print(f"Телефон: {self.phone}")
        print(f"Часы работы: {self.working_hours}")
        print("Ассортимент: Любые цветы на ваш вкус")
        for item, price in self.items.items():
            print(f" - {item}: {price} руб.")

# Создание объектов класса Store
store1 = Store("Студия цветов", "ул. Весенняя, 40",
                "Специализируемся на создании уникальных букетов.",
                "+7 (123) 456-78-90",
                "09:00 - 20:00")

store2 = Store("Букетик", "ул. Дачная, 5",
                "Магазин свежих цветов и подарков.",
                "+7 (123) 987-65-43",
                "10:00 - 19:00")

store3 = Store("Цветочный дворик", "ул. Дружбы, 21",
                "Широкий ассортимент растений и аксессуаров.",
                "+7 (123) 654-32-10",
                "08:00 - 21:00")

# Вывод информации о магазинах
print("\nИнформация о магазинах сети 'Цветочный рай':")
store1.display_info()
store2.display_info()
store3.display_info()

# Добавление товаров в магазины
store1.add_item("ромашки", 150)
store1.add_item("астры", 200)
store2.add_item("астры", 210)
store3.add_item("пионы", 240)
store3.add_item("ромашки", 155)

# Тестирование методов на примере store1
print("\nТестирование методов для магазина 'Студия цветов':")
store1.add_item("тюльпаны", 180)  # Добавление товара
store1.update_price("ромашки", 170)  # Обновление цены
print(f"Цена ромашек: {store1.get_price('ромашки')}")  # Запрос цены
store1.remove_item("астры")  # Удаление товара
print(f"Цена астр: {store1.get_price('астры')}")  # Запрос цены после удаления

