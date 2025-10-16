import re
txt=input()
x=re.findall(r"[A-Z][a-z]+",txt) #что бы найти слово где одна заглавная и остальные строчные
print(x)