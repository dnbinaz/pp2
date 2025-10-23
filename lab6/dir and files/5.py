def write_list_to_file(path, data):
    with open(path, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')

write_list_to_file("output.txt", ["Item 1", "Item 2", "Item 3", "Item 4"])
