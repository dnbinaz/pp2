import re
txt=input()
x=re.sub(r"[., ]",":",txt) #заменить все пробелы точки и запятые двоеточием
print(x)