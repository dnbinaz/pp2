import math

def regular_polygon_area(num_sides, side_length):
    apothem = side_length / (2 * math.tan(math.pi / num_sides))
    area = (num_sides * side_length * apothem) / 2
    return area

num_sides = int(input("Enter the number of sides of the regular polygon: "))
side_length = float(input("Enter the length of a side of the regular polygon: "))

result = regular_polygon_area(num_sides, side_length)

print(f"Number of sides: {num_sides}")
print(f"Length of a side: {side_length}")
print(f"The area of the regular polygon is: {result}")
