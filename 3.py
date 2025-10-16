import re
txt=input()
x=re.findall(r"[a-z_]+_[a-z]+",txt) #найти строчные буквы соединенные символом подчеркивания
print(x)