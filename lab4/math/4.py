def parallelogram_area(base_length, height):
    area = base_length * height
    return area

base_length = float(input("Enter the length: "))
height = float(input("Enter the height: "))

result = parallelogram_area(base_length, height)
print(f"The area of the parallelogram is: {result}")
