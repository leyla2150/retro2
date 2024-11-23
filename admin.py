class User:
    def __init__(self, user_id, name):
        self.user_id = user_id  # ID пользователя (защищенный атрибут)
        self.name = name  # Имя пользователя (защищенный атрибут)
        self.__access_level = 'user'  # Уровень доступа для обычных пользователей

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self.user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self.name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name)  # Инициализация родительского класса
        self.__access_level = access_level  # Уровень доступа для администраторов

    # Метод для добавления пользователя
    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: Это не пользователь.")

    # Метод для удаления пользователя
    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Ошибка: Пользователь не найден.")

    # Метод для поиска пользователя по имени
    def find_user_by_name(self, user_list, name):
        for user in user_list:
            if user.get_name() == name:
                print("Найден")
                return user
        print("Не найден")
        return None

# Пример использования классов
if __name__ == "__main__":
    # Список пользователей
    user_list = []

    # Создание обычных пользователей
    user1 = User(1, "Иван Иванов")
    user2 = User (2, "Анна Петрова")
    user3 = User(3, "Петр Сидоров")
    # Создание администратора
    admin = Admin(4, "Сергей Серов")

    # Администратор добавляет пользователей
    admin.add_user(user_list, user1)
    admin.add_user(user_list, user2)
    admin.add_user(user_list, user3)

    # Вывод списка пользователей
    print("\nСписок пользователей:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Администратор удаляет пользователя
    admin.remove_user(user_list, 1)

    # Вывод обновленного списка пользователей
    print("\nОбновленный список пользователей:")
    for user in user_list:
        print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

    # Поиск пользователя по имени
    name_to_find = input("\nВведите имя пользователя для поиска: ")
    admin.find_user_by_name(user_list, name_to_find)  # Найден или не найден
