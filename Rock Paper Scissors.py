import random

# Greeting
play_or_no = input("Welcome to a game of Rock Paper Scissors, would you like to play? (Yes/No): ").lower()

# Main
while play_or_no == "yes":
https://github.com/
    random_number = random.randint(1, 3)

    # User's choice
    user_input = input("Rock, Paper, or Scissors?: ").lower()
    choices = ["rock", "paper", "scissors"]
    if user_input not in choices:
        print("Please enter either rock paper or scissors")
        continue

    # Computer's choice
    if random_number == 1:
        comp = "rock"
        print("Computer chose: rock")
    elif random_number == 2:
        comp = "paper"
        print("Computer chose: paper")
    elif random_number == 3:
        comp = "scissors"
        print("Computer chose: scissors")

    # Compare choices
    if user_input == "rock" and comp == "paper":
        print("You lose")
        print("--------")
    elif user_input == "paper" and comp == "scissors":
        print("You lose")
        print("--------")
    elif user_input == "scissors" and comp == "rock":
        print("You lose")
        print("--------")
    elif user_input == comp:
        print("Tie")
        print("---")
    else:
        print("You win")
        print("-------")

    # Replay
    while True:
        play_again = input("Would you like to play again? (Yes/No): ").lower()
        if play_again in ("yes", "no"):
            break
        print("Please enter yes or no")
    if play_again == "yes":
        continue

    else:
        print("Ok thank you for playing, have a good day!")
        break
else:
    print("Ok have a good day")
