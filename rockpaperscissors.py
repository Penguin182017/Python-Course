import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0


# Function to determine winner
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

    # Conditions
    if user_choice == computer_choice:
        result_text += "Result: It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_text += "Result: You Win!"
        user_score += 1
    else:
        result_text += "Result: Computer Wins!"
        computer_score += 1

    # Update labels
    result_label.config(text=result_text)

    score_label.config(
        text=f"Your Score: {user_score}    Computer Score: {computer_score}"
    )


# Reset game function
def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    result_label.config(text="Choose Rock, Paper, or Scissors")
    score_label.config(text="Your Score: 0    Computer Score: 0")


# Main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x350")
root.config(bg="lightblue")


# Title
title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)
title_label.pack(pady=10)


# Result label
result_label = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
result_label.pack(pady=20)


# Buttons Frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)


# Rock Button
rock_button = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    command=lambda: play("Rock")
)
rock_button.grid(row=0, column=0, padx=5)


# Paper Button
paper_button = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    command=lambda: play("Paper")
)
paper_button.grid(row=0, column=1, padx=5)


# Scissors Button
scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    command=lambda: play("Scissors")
)
scissors_button.grid(row=0, column=2, padx=5)


# Score label
score_label = tk.Label(
    root,
    text="Your Score: 0    Computer Score: 0",
    font=("Arial", 12, "bold"),
    bg="lightblue"
)
score_label.pack(pady=20)


# Reset button
reset_button = tk.Button(
    root,
    text="Reset Game",
    width=15,
    command=reset_game
)
reset_button.pack(pady=10)


# Exit button
exit_button = tk.Button(
    root,
    text="Exit",
    width=15,
    command=root.destroy
)
exit_button.pack(pady=5)


# Run window loop
root.mainloop()