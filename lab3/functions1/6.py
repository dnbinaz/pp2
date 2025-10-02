def reverse_words(sentence):
    # Разделили предложение на слова
    words = sentence.split()

    # Изменяем порядок слов и выводим их
    #Оператор * распаковки используется для передачи элементов перевернутого списка в качестве отдельных аргументов функции print
    print(*reversed(words))

user_input = input("Enter a sentence: ")
reverse_words(user_input)