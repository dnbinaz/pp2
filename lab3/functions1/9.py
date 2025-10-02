import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

user_radius = float(input("Enter the radius of the sphere: "))

# Вызов функции sphere_volume с пользовательским вводом
volume = sphere_volume(user_radius)
print(volume)