import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Define global variables
button_enabled = False
rounds_to_play = 3
player_score = 0
computer_score = 0
current_round = 0
round_counter=0

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    round_counter=0
    round_counter=round_counter+1
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle player's choice
def player_choice(choice):
    global button_enabled, player_score, computer_score, current_round
    if not button_enabled and round_counter==3:
        rock_btn.config(state="disabled")
        paper_btn.config(state="disabled")
        scissors_btn.config(state="disabled")
        button_enabled = True

    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    result = determine_winner(choice, computer_choice)
    update_score(result)
    result_label.config(text=result)

    player_choice_label.config(text=f"User: {choice.capitalize()}")
    computer_choice_label.config(text=f"Computer: {computer_choice.capitalize()}")

    current_round += 1
    if current_round >= rounds_to_play:
        end_game()

# Function to update the score
def update_score(result):
    global player_score, computer_score
    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    player_score_label.config(text=f"Your Score: {player_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to end the game and display the final result
def end_game():
    global button_enabled
    if player_score > computer_score:
        result_label.config(text="Congratulations! You won the game!")
    elif player_score < computer_score:
        result_label.config(text="Computer wins the game!")
    else:
        result_label.config(text="It's a tie!")
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")
    reset_btn.grid(row=5, column=0, columnspan=3, pady=10)
    round_counter=0

# Function to reset the game and start a new game
def reset_game():
    global button_enabled, player_score, computer_score, current_round
    button_enabled = False
    player_score = 0
    computer_score = 0
    current_round = 0
    result_label.config(text="")
    player_choice_label.config(text="")
    computer_choice_label.config(text="")
    player_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")
    reset_btn.grid_forget()

# GUI setup
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("700x450")
root.resizable(False, False)  # Disable resizing

# Load images
rock_img = Image.open("rock.png")
rock_img = rock_img.resize((200, 200), Image.ANTIALIAS)
rock_photo = ImageTk.PhotoImage(rock_img)

paper_img = Image.open("paper.png")
paper_img = paper_img.resize((200, 200), Image.ANTIALIAS)
paper_photo = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open("scissors.png")
scissors_img = scissors_img.resize((200, 200), Image.ANTIALIAS)
scissors_photo = ImageTk.PhotoImage(scissors_img)

# Buttons
rock_btn = tk.Button(root, image=rock_photo, command=lambda: player_choice('rock'))
rock_btn.grid(row=0, column=0, padx=10, pady=10, sticky="e")

paper_btn = tk.Button(root, image=paper_photo, command=lambda: player_choice('paper'))
paper_btn.grid(row=0, column=1, padx=10, pady=10)

scissors_btn = tk.Button(root, image=scissors_photo, command=lambda: player_choice('scissors'))
scissors_btn.grid(row=0, column=2, padx=10, pady=10, sticky="w")

# Labels
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=1, column=0, columnspan=3)

player_choice_label = tk.Label(root, text="", font=("Arial", 12))
player_choice_label.grid(row=2, column=0, columnspan=3)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.grid(row=3, column=0, columnspan=3)

player_score_label = tk.Label(root, text="Your Score: 0", font=("Arial", 12))
player_score_label.grid(row=4, column=0, padx=10, pady=10)

computer_score_label = tk.Label(root, text="Computer's Score: 0", font=("Arial", 12))
computer_score_label.grid(row=4, column=1, padx=10, pady=10)

# Reset Button
reset_btn = tk.Button(root, text="Reset", command=reset_game)

root.mainloop()

