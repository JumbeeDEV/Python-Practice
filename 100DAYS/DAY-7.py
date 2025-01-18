import random

end_of_game = False

wordlist = ["istanbul", "paris", "tokyo"]
chosen_word = random.choice(wordlist)
print(chosen_word)

display = []
while not end_of_game:
    for char in chosen_word:
        display += "_"
    user_guess = input("Guess a letter: ").lower()
    

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    if "_" not in display:
        end_of_game = True
        print("You win")
    else:
        print("try again")
    
print("game over")


