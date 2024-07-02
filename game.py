import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score}  Computer Score: {computer_score}")

# Function to reset the game
def reset_game():
    result_label.config(text="")
    
# Function to exit the game
def exit_game():
    root.destroy()
    
# Main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg='#333')

# Labels and Buttons
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Helvetica", 14), fg='white', bg='#333')
instructions_label.pack(pady=20)

rock_button = tk.Button(root, text="Rock", width=20, command=lambda: determine_winner("Rock"), bg='#00f', fg='white')
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, command=lambda: determine_winner("Paper"), bg='#00f', fg='white')
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, command=lambda: determine_winner("Scissors"), bg='#00f', fg='white')
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), fg='white', bg='#333')
result_label.pack(pady=20)

score_label = tk.Label(root, text="Your Score: 0  Computer Score: 0", font=("Helvetica", 14), fg='white', bg='#333')
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Play Again", width=20, command=reset_game, bg='#ffa500', fg='white')
reset_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=exit_game, bg='#888', fg='white')
exit_button.pack(pady=5)

# Run the application
root.mainloop()