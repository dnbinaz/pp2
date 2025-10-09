def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for number in countdown_generator(n):
    print(number)