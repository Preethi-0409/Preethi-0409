import random

words = ["apple", "tiger", "chair", "table", "phone"]
word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if display == word:
        print("You won!")
        break

    guess = input("Guess letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("You lost. Word was:", word)