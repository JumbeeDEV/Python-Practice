import random

wordlist = ["istanbul", "paris", "tokyo"]

chosen_word = random.choice(wordlist)

print(chosen_word)

user_guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == user_guess:
        print("Right")