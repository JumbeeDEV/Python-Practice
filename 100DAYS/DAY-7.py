import random

end_of_game = False

wordlist = ["istanbul", "paris", "tokyo"]
chosen_word = random.choice(wordlist)
print(chosen_word)

display = ["_" for _ in chosen_word]
guessed_letters = set()

while not end_of_game:
    print(display)
    user_guess = input("Guess a letter: ").lower()
    if user_guess in guessed_letters:
        print("you already guessed this letter")
        continue
    guessed_letters.add(user_guess)

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    if "_" not in display:
        end_of_game = True
        print("You win")
        print(display)
    else:
        print("try again")
    
print("game over")
