import math
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

input_degree = float(input("Enter the degree value: "))
output_radian = degrees_to_radians(input_degree)
print(output_radian)