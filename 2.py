import re
txt=input()
x=re.search(r"ab{2,3}",txt) #после а 2-3 б
print(x)