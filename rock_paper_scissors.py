#Coded by Mohammad Salam


import random

user_total_wins = 0
computer_total_wins = 0 

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nType 1 for Rock, 2 for Paper, 3 for Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    try:
        user_choice = int(user_input)
        if user_choice not in [1, 2, 3]:
            continue
    except ValueError:
        continue

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_picks = "rock"
    elif computer_choice == 2:
        computer_picks = "paper"
    else:
        computer_picks = "scissors"

    print("\nComputer picked", computer_picks + ".")

    if user_choice == 1 and computer_choice == 3:
        print("You won!\n")
        user_total_wins += 1
        
    elif user_choice == 2 and computer_choice == 1:
        print("You won!\n")
        user_total_wins += 1

    elif user_choice == 3 and computer_choice == 2:
        print("You won!\n")
        user_total_wins += 1
    
    else:
        print("You lost!\n")
        computer_total_wins += 1
print("===================================")
print("You won", user_total_wins, "times.")
print("The computer won", computer_total_wins, "times.") 
print("===================================")
print("Goodbye!")
