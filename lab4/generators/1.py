def generate_squares(N):
    for i in range(N+1):
        yield i ** 2
N = int(input())
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)