import re
txt=input()
x = re.findall(r"[A-Z][^A-Z]*", txt) #что бы вставить пробелы между слов начинающиеся с заглавной буквы
res=' '.join(x)
print(res)