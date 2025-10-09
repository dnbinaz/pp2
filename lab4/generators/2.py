def even_num(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i
n=int(input())
N=even_num(n)
for even in N:
    print(even)
