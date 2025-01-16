import random

rock = "🪨"
paper = "🧻"
scissors = "✂️"

rock_paper_scissors = ["rock","paper","scissors"]
#print(rock_paper_scissors)
user_Selection = input(f"which do you chose {rock_paper_scissors}:\n -for rock type rock\n -for paper type paper\n -for scissors type scissors")

computer_Selection = random.choice(rock_paper_scissors)

if user_Selection ==  computer_Selection:
    print("its draw")
elif user_Selection == "rock" and computer_Selection == "paper":
    print(f"You chose rock {rock} and the computer chose paper {paper}. Computer wins!")
elif user_Selection == "rock" and computer_Selection == "scissors":
    print(f"You chose rock {rock} and the computer chose scissors {scissors}. You win!")
elif user_Selection == "paper" and computer_Selection == "rock":
    print(f"You chose paper {paper} and the computer chose rock {rock}. You win!")
elif user_Selection == "paper" and computer_Selection == "scissors":
    print(f"You chose paper {paper} and the computer chose scissors {scissors}. Computer wins!")
elif user_Selection == "scissors" and computer_Selection == "rock":
    print(f"You chose scissors {scissors} and the computer chose rock {rock}. Computer wins!")
elif user_Selection == "scissors" and computer_Selection == "paper":
    print(f"You chose scissors {scissors} and the computer chose paper {paper}. You win!")
else:
    print("Invalid selection. Please type 'rock', 'paper', or 'scissors'.")


