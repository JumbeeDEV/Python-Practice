import random

end_of_game = False

wordlist = ["istanbul", "paris", "tokyo"]
chosen_word = random.choice(wordlist)
print(chosen_word)

display = []
while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == user_guess:
            display.append(letter)
        elif letter != user_guess:
            display += "_"

    print(display)



if "_" not in display:
    end_of_game = True
    print("You win")


