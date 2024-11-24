class Task:
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи
        self.deadline = deadline  # Срок выполнения
        self.completed = False  # Статус задачи (выполнено/не выполнено)

    def mark_completed(self):
        self.completed = True  # Отметка задачи как выполненной

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок выполнения: {self.deadline}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)  # Добавление новой задачи в список

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()  # Отметка задачи как выполненной
        else:
            print("Неверный индекс задачи.")

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]  # Список текущих задач

    def display_tasks(self):
        if not self.tasks:
            print("Нет задач для отображения.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")


# Пример использования
task_manager = TaskManager()

# Добавление задач
task_manager.add_task(description="Сделать домашнее задание", deadline="25.11.2024")
task_manager.add_task(description="Подготовиться к экзамену", deadline="26.11.2024")

# Отображение текущих задач
print("Текущие задачи:")
task_manager.display_tasks()

# Отметка первой задачи как выполненной
task_manager.mark_task_completed(0)

# Отображение текущих задач после отметки
print("\nТекущие задачи после отметки:")
task_manager.display_tasks()
