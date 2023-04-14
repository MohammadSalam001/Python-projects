#Coded by Mohammad Salam


import random
import tkinter as tk

user_total_wins = 0
computer_total_wins = 0 

choices = ["rock", "paper", "scissors"]

# Create a Tkinter window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")
window.option_add("*Font", "Arial 24 bold")
window.configure(bg='grey')



#Size of window
window.geometry("1500x500")

# Create a label widget to display the computer's choice
computer_label = tk.Label(window, text="Computer picks: ", bg='grey')
computer_label.pack()

# Create a label widget to display the game result
result_label = tk.Label(window, text="", bg="grey")
result_label.pack()

# Function to handle user input
def handle_user_input(choice):
    global user_total_wins, computer_total_wins
    if choice == 4:
        window.destroy()
        return
    try:
        user_choice = int(choice)
        if user_choice not in [1, 2, 3]:
            return
    except ValueError:
        return

    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_picks = "rock"
    elif computer_choice == 2:
        computer_picks = "paper"
    else:
        computer_picks = "scissors"

    computer_label.config(text="Computer picks: " + computer_picks)

    if user_choice == 1 and computer_choice == 3:
        result_label.config(text="You won!")
        user_total_wins += 1
        
    elif user_choice == 2 and computer_choice == 1:
        result_label.config(text="You won!")
        user_total_wins += 1

    elif user_choice == 3 and computer_choice == 2:
        result_label.config(text="You won!")
        user_total_wins += 1
    
    else:
        result_label.config(text="You lost!")
        computer_total_wins += 1

    # Update the game statistics
    stats_label.config(text="You won " + str(user_total_wins) + " times.\nThe computer won " + str(computer_total_wins) + " times.")

# Create buttons for the user to select their choice
rock_button = tk.Button(window, text="Rock", command=lambda: handle_user_input(1), width=10, height=5)
rock_button.pack(side="left", padx=10, pady=10)

paper_button = tk.Button(window, text="Paper", command=lambda: handle_user_input(2), width=10, height=5)
paper_button.pack(side="left", padx=10, pady=10)

scissors_button = tk.Button(window, text="Scissors", command=lambda: handle_user_input(3), width=10, height=5)
scissors_button.pack(side="left", padx=10, pady=10)

quit_button = tk.Button(window, text="Quit Game", command=lambda: handle_user_input(4), width=10, height=5)
quit_button.pack(side="left", padx=10, pady=10)


# Create a label widget to display the game statistics

live_score_line1 = tk.Label(window, text="--------------------------", bg='#FF0001', fg= "white" )
live_score_label = tk.Label(window, text="--- LIVE SCORE ----", bg='#FF0001', fg= "white" )
live_score_line2 = tk.Label(window, text="--------------------------", bg='#FF0001',fg= "white" )

newline= tk.Label(window, text="\n", bg="grey")
stats_label = tk.Label(window, text="You won 0 times.\nThe computer won 0 times.", bg='#89CFF0')

live_score_line1.pack()
live_score_label.pack()
live_score_line2.pack()
newline.pack()
stats_label.pack()

# Start the main loop for the Tkinter window
window.mainloop()
