import tkinter as tk
def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)
def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, {'bg': 'slate blue'})
root = tk.Tk()
root.title("Ежедневник")
root.configure(background="dark red")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="CadetBlue1")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_task_button = tk.Button(button_frame, text="Добавить задачу", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Удалить задачу", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)
text2 = tk.Label(root, text="Список задач:", bg="bisque1")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=20, width=80, bg="burlywood")
task_listBox.pack(pady=10)

root.mainloop()