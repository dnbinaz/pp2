import re
txt=input()
x=re.findall(r"a.*b$",txt) #начинается на а и заканчивается на б
print(x)