def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    print(f"The number of uppercase letters: {upper_count}")
    print(f"The number of lowercase letters: {lower_count}")

input_string = "Hello World! Python Programming"
count_upper_lower(input_string)
