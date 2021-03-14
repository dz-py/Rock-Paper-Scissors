import random

# Greeting
play_or_not = input("Welcome to a game of Rock Paper Scissors. Would you like to play? (Yes/No): ").lower()

# Main
while play_or_not == "yes":

    random_number = random.randint(1, 3)
    # User's choice
    user_input = input("Rock, Paper, or Scissors?: ").lower()

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
    elif user_input == "paper" and comp == "scissors":
        print("You lose")
    elif user_input == "scissors" and comp == "rock":
        print("You lose")
    elif user_input == comp:
        print("Tie")
    else:
        print("You win")
    play_or_not = input("Would you like to play again? (Yes/No): ").lower()

else:
    print("Ok have a good day")
