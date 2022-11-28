import random


def choices():
    # function to display new game

    player = input("enter your name\t")
    name = player
    # function that requires the user to enter their input
    player_choice = input("enter a choice between rock paper and scissors\t")
    options = ["rock", "paper", "scissors"]
    # a function that makes the computer choose between the options at random
    computer_choice = random.choice(options)
    choices = {name: player_choice, "computer": computer_choice}
    print(f"computer:", computer_choice)
    # assigning what will be displayed after win is checked
    message1 = "its a tie"
    message2 = "you have lost"
    message3 = "you have won"
    # checking who has won
    if player_choice == computer_choice:
        print(message1)
    elif player_choice == "rock" and computer_choice == "scissors":
        print(message3)
    elif player_choice == "rock" and computer_choice == "paper":
        print(message2)
    elif player_choice == "paper" and computer_choice == "scissors":
        print(message2)
    elif player_choice == "paper" and computer_choice == "rock":
        print(message3)
    elif player_choice == "scissors" and computer_choice == "paper":
        print(message3)
    else:
        print(message2)


choices()
