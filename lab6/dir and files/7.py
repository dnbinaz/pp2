with open('smthg.txt', 'r') as src:
    content = src.read()

with open('test.txt', 'w') as dst:
    dst.write(content)

print("Copied successfully.")
