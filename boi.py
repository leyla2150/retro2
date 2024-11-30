# Программа "Битва"

from abc import ABC, abstractmethod
import random

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретный класс для меча
class Sword(Weapon):
    def attack(self):
        damage = random.randint(10, 20)  # Удар мечом
        return damage

# Конкретный класс для лука
class Bow(Weapon):
    def attack(self):
        damage = random.randint(5, 15)  # выстрел из лука
        return damage

# Класс для бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = None  # Поле для хранения объекта Weapon

    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} выбрал {weapon.__class__.__name__}")

    def attack(self):
        if self.weapon:
            damage = self.weapon.attack()
            print(f"{self.name} наносит удар {self.weapon.__class__.__name__} и наносит {damage} удар")
            return damage
        else:
            print(f"{self.name} не имеет оружия!")
            return 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} удар, количество жизней: {self.health}")
        if self.health <= 0:
            print(f"{self.name} пал в бою!")

# Класс для монстра
class Monster:
    def __init__(self, name):
        self.name = name
        self.health = 50

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} удар, количество жизней- {self.health}")
        if self.health <= 0:
            print(f"{self.name}  побежден!")

# начало игры
def game():
    fighter_name = input("Введите имя бойца: ")
    fighter = Fighter(fighter_name)
    monster_name = "Монстр"
    monster = Monster(monster_name)
    weapons = [Sword(), Bow()]

    # Боец выбирает оружие
    for i, weapon in enumerate(weapons):
        print(f"{i + 1} - {weapon.__class__.__name__}")
    weapon_choice = int(input("Выберите оружие (1 или 2): "))
    fighter.change_weapon(weapons[weapon_choice - 1])

    # Бой
    while fighter.health > 0 and monster.health > 0:
        damage = fighter.attack()
        monster.take_damage(damage)

        if monster.health > 0:
            damage_to_fighter = random.randint(5, 10)  # Удар от монстра
            print(f"{monster.name} атакует {fighter.name} и наносит {damage_to_fighter} удар")
            fighter.take_damage(damage_to_fighter)

    print("Игра окончена!")

# Запуск игры
if __name__ == "__main__":
    game()


