import os

path = r'/Users/ihlasova75icloud.com/Desktop/pp2/lab6'
print("Existence:", os.path.exists(path))
print("Read access:", os.access(path, os.R_OK))
print("Write access:", os.access(path, os.W_OK))
print("Execute access:", os.access(path, os.X_OK))
