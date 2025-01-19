# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.

with open("task3.txt", encoding="utf-8") as f:
    string = f.read()

string = string.lower()

if "—" in string:
    string = string.replace("—", "")
if "." in string:
    string = string.replace(".", '')
if "," in string:
    string = string.replace(",", '')

words = string.split()
words_formated = list(set(words))
ans = open("task3Answer.txt", 'w', encoding="utf-8")
Ans = []
for i in range(0, len(words_formated)):
    Ans.append(str(f"{words_formated[i]}: {words.count(words_formated[i])}\n"))

Ans.sort()
for j in range(0, len(Ans)):
    ans.write(Ans[j])
print(words)



