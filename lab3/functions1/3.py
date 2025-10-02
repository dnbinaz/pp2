def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2*num_chickens + 4*num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits

num_heads = 35
num_legs = 94

chickens, rabbits = solve(num_heads, num_legs)
print(chickens)
print(rabbits)
