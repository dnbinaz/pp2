def all_true(elements):
    return all(elements)

tuple_1 = (True, True, True, True)
tuple_2 = (True, False, True, True)

result_1 = all_true(tuple_1)
result_2 = all_true(tuple_2)

print(f"All elements of tuple_1 are True: {result_1}")
print(f"All elements of tuple_2 are True: {result_2}")
