import random

value = random.randint(1, 20)

number_of_guesses = 0

guess = 0

while guess != value:
    print("What is your guess?")
    guess = input()
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1

    if guess == value:
        print("Congratz! You guessed right in " + str(number_of_guesses) + " guesses!")

    if guess < value:
        print("Your guess is too low!")

    if guess > value:
        print("Your guess is too high!")