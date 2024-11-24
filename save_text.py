# Запрашиваем у пользователя текст
user_input = input("Введите текст для сохранения в файл user_data.txt: ")

# Открываем файл в режиме записи и записываем текст
with open('user_data.txt', 'w', encoding='utf-8') as file:
    file.write(user_input)

print("Текст успешно сохранен в файл user_data.txt.")

# Открываем файл в режиме чтения и выводим содержимое
with open("user_data.txt", 'r', encoding='utf-8') as file:
    saved_text = file.read()
    print("Сохраненный текст:", saved_text)