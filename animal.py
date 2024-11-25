class Animal:
    def __init__(self, species, age, habitat):
        self.species = species  # Вид животного
        self.age = age          # Возраст животного
        self.habitat = habitat  # Среда обитания

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")

    def info(self):
        return f"Вид: {self.species}, Возраст: {self.age}, Среда обитания: {self.habitat}"

class Bird(Animal):
    def __init__(self, species, age, habitat, wing_span):
        super().__init__(species, age, habitat)
        self.wing_span = wing_span  # Размах крыльев

    def make_sound(self):
        return f"{self.species} чирикает."

class Mammal(Animal):
    def __init__(self, species, age, habitat, height):
        super().__init__(species, age, habitat)
        self.height = height  # Высота млекопитающего

    def make_sound(self):
        return f"{self.species} рычит."

class Reptile(Animal):
    def __init__(self, species, age, habitat, scale_type):
        super().__init__(species, age, habitat)
        self.scale_type = scale_type  # Тип чешуи

    def make_sound(self):
        return f"{self.species} шипит."

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []    # Список животных в зоопарке
        self.employees = []  # Список сотрудников зоопарка

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено: {animal.species} в зоопарк.")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен {employee.name} в штат зоопарка.")

    def show_animals_info(self):
        for animal in self.animals:
            print(animal.info())

class Veterinarian:
    def __init__(self, name):
        self.name = name  # Имя ветеринара

    def heal_animal(self, animal):
        return f"{self.name} на лечении - {animal.species}."

# Создание животных
parrot = Bird("Попугай", 2, "Тропики", "30 cm")
lion = Mammal("Лев", 5, "Саванна", "1.2 m")
snake = Reptile("Змея", 3, "Степь", "гладкая")

# Демонстрация полиморфизма
animal_sound([parrot, lion, snake])

# Создание зоопарка и добавление животных
zoo = Zoo()
for animal in [parrot, lion, snake]:
    zoo.add_animal(animal)

# Вывод информации о животных в зоопарке
print("\nИнформация о животных в зоопарке:")
zoo.show_animals_info()

# Создание ветеринара и лечение животного
vet = Veterinarian("Доктор Поляков: ")
print(vet.heal_animal(lion))
