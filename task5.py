# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.

with open("task5.txt", encoding="utf-8") as f:
    string = f.read()

string = string.lower()
if "—" in string:
    string = string.replace("—", "")
if "." in string:
    string = string.replace(".", '')
if "," in string:
    string = string.replace(",", '')
if "!" in string:
        string = string.replace("!", '')
words = string.split()
lens = []
for i in range(0, len(words)):
    lens.append(len(words[i]))
Key = lens.index(max(lens))

with open("task5Answer.txt", "w", encoding="utf-8") as f:
    f.write(f"Самое длинное слово: {words[Key]}\nЕго длина: {len(words[Key])}")
