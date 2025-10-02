import random
def guess_the_number():
    
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randrange(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        user_guess = int(input())
        guesses_taken += 1

        if user_guess < secret_number:
            print("Your guess is too low.")
        elif user_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()