def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime(numbers_list)
print(result)

#The is_prime function checks whether a given number n is prime or not.
#The filter_prime function uses list comprehension to create a new list containing only the prime numbers from the input list.
