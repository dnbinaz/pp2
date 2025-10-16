import re
txt=input()
x=re.findall(r"[^A-Z]*[A-Z][^A-Z]*",txt) #разделение строк на заглавные буквы
result=' '.join(x)
print(result)