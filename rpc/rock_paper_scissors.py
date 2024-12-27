import random

def get_user_choice():
    users_choice = input("Enter rock, paper or scissors?('q' if you want to quit) ")
    return users_choice

def get_computer_choice():
    computers_choice = random.choice(["rock", "paper", "scissors"])
    return computers_choice


choices = ['rock', 'paper', 'scissors']
while True:
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    if user_choice == 'q':
        print("Good Bye")
        exit(0)

    else:
        if user_choice in choices:
            print(f"You chose '{user_choice}' and computer chose '{computer_choice}'")
            if user_choice == computer_choice:
                print("It's a TIE!")

            elif computer_choice == 'rock' and user_choice == 'paper':
                print("you win!")

            elif computer_choice == 'paper' and user_choice == 'scissors':
                print("you win!")

            elif computer_choice == 'scissors' and user_choice == 'rock':
                print("you win!")

            else:
                print("Computer wins!")
        else:
            print("Invalid opiton")