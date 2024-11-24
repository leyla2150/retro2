class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
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


# Создание объектов класса Store
store1 = Store("Студия цветов", "ул. Весенняя, 40")
store2 = Store("Букетик", "ул. Дачная, 5")
store3 = Store("Цветочный дворик", "ул. Дружбы, 21")

# Добавление товаров в магазины
store1.add_item("ромашки", 150)
store1.add_item("астры", 200)
store1.add_item("пионы", 250)

store2.add_item("ромашки", 160)
store2.add_item("астры", 210)

store3.add_item("пионы", 240)
store3.add_item("астры", 220)
store3.add_item("ромашки", 155)

# Тестирование методов на примере store1
print("\nТестирование методов для магазина 'Студия цветов':")
store1.add_item("тюльпаны", 180)  # Добавление товара
store1.update_price("ромашки", 170)  # Обновление цены
print(f"Цена ромашек: {store1.get_price('ромашки')}")  # Запрос цены
store1.remove_item("астры")  # Удаление товара
print(f"Цена астр: {store1.get_price('астры')}")  # Запрос цены после удаления
