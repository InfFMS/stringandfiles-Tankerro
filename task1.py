# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.

f=open("task1.txt", encoding="utf-8")
lines = len(f.readlines())
f=open("task1.txt", encoding="utf-8")
string = f.read()
words = string.split()
words.remove("—")
words = len(words)
f=open("task1.txt", encoding="utf-8")
string = f.read()
chars = len(string)
print(lines)
print(words)
print(chars)
f.close()