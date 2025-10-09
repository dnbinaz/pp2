def trapezoid_area(height, base1, base2):
    area = 0.5 * (base1 + base2) * height
    return area

height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("first base of the trapezoid: "))
base2 = float(input("second base of the trapezoid: "))
result = trapezoid_area(height, base1, base2)

print(f"Area of the trapezoid: {result}")