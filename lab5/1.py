import re
txt=input()
x=re.search("ab*",txt) #ищет строку где за а следует б
print(x)