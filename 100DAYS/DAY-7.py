import random

wordlist = ["istanbul", "paris", "tokyo"]

chosen_word = random.choice(wordlist)

print(chosen_word)

for char in chosen_word:
    print("_" , end=" ")

user_guess = input("Guess a letter: ").lower()
for letter in chosen_word:
    if letter == user_guess:
        print(letter, end = " ")
    elif letter != user_guess:
        print("_", end = " ") 
    
