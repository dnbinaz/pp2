def spy_game(nums):
    # Инициализируeм переменную, чтобы отслеживать текущую позицию в последовательности
    sequence_position = 0
    
    # Выполнить итерацию по списку
    for num in nums:
        # Проверяем совпадает ли текущее число со следующей ожидаемой цифрой в последовательности
        if num == 0 and sequence_position == 0:
            sequence_position += 1
        elif num == 0 and sequence_position == 1:
            sequence_position += 1
        elif num == 7 and sequence_position == 2:
            return True

    # Если цикл завершается без нахождения последовательности, возвращает значение False
    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  