# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.

with open("task2.txt", encoding="utf-8") as f:
    string = f.read()
changes_count = 0
while string.find("Python") != -1:
    string = string[:string.find("Python")] + "Питон" + string[string.find("Python")+6:]
    changes_count += 1
print(f"{string}\nКоличество замен: {changes_count}")
