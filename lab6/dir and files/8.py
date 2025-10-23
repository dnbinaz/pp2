import os

path = r'/Users/ihlasova75icloud.com/Desktop/pp2/lab6/dir and files/AUTHORS.txt'

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"File '{path}' removed successfully.")
    else:
        print("No access rights to delete this file.")
else:
    print("File does not exist.")
