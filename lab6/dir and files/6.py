import os

def generate_text_files():
    for letter in range(ord('A'), ord('Z') + 1):
        file_name = f"{chr(letter)}.txt"
        with open(file_name, 'w') as file:
            file.write(f"Content for file {file_name}")

        print(f"File '{file_name}' created successfully.")

generate_text_files()
