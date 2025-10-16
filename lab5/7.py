import re
txt=input()
x=re.sub(r"[_]","",txt)  #соеденить слова вместо нижниего подчеркивания
print(x)