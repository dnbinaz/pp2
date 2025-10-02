def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit_inp= float(input())
print(fahrenheit_to_celsius(fahrenheit_inp))
