import tkinter as tk
import random

# Original logic variables
n = random.randint(1, 100)
a = -1
guesses = 0

# Restart game function
def restart_game():
    global n, a, guesses
    n = random.randint(1, 100)
    a = -1
    guesses = 0
    entry.delete(0, tk.END)
    result_label.config(text="")
    guess_label.config(text=" Attempts: 0 ")

# Custom styled popup function
def cute_popup(title, message):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("400x220")
    popup.config(bg="#fff0f5")

    msg_label = tk.Label(popup, text=message, font=("Comic Sans MS", 14, "bold"), bg="#fff0f5", fg="#ff3399", wraplength=350, justify="center")
    msg_label.pack(pady=20)

    btn_frame = tk.Frame(popup, bg="#fff0f5")
    btn_frame.pack(pady=10)

    ok_btn = tk.Button(btn_frame, text=" Exit ", command=root.destroy, font=("Comic Sans MS", 12, "bold"), bg="#ffb3d9", fg="#660066", relief="raised", bd=3, padx=10, pady=5)
    ok_btn.grid(row=0, column=0, padx=10)

    play_again_btn = tk.Button(btn_frame, text=" Play Again ", command=lambda: (popup.destroy(), restart_game()), font=("Comic Sans MS", 12, "bold"), bg="#b3ffd9", fg="#004d33", relief="raised", bd=3, padx=10, pady=5)
    play_again_btn.grid(row=0, column=1, padx=10)

# Function for button click
def check_guess():
    global a, guesses
    try:
        a = int(entry.get())
        guesses += 1
        guess_label.config(text=f" Attempts: {guesses} ")

        if a < n:
            result_label.config(text=" Higher number Please ", fg="#ff66b2")
        elif a > n:
            result_label.config(text=" Lower number Please ", fg="#9966ff")
        else:
            cute_popup(" Congratulations! ", f"You guessed the number {n} correctly in {guesses} attempts!")
    except ValueError:
        result_label.config(text=" Please enter a valid number! ", fg="red")

# GUI setup
root = tk.Tk()
root.title(" Cute Number Guessing Game ")
root.geometry("450x320")
root.config(bg="#fff0f5")  # Light pink background

# Instruction label
instruction = tk.Label(root, text=" Guess a number between 1 and 100 ", font=("Comic Sans MS", 14, "bold"), bg="#fff0f5", fg="#ff3399")
instruction.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Comic Sans MS", 14), justify="center", bg="#ffe6f0", fg="#660033", relief="ridge", bd=3)
entry.pack(pady=8)

# Button
check_btn = tk.Button(root, text="Check ", command=check_guess, font=("Comic Sans MS", 12, "bold"), bg="#ffb3d9", fg="#660066", relief="raised", bd=3, padx=10, pady=5)
check_btn.pack(pady=8)

# Result label
result_label = tk.Label(root, text="", font=("Comic Sans MS", 13, "italic"), bg="#fff0f5")
result_label.pack(pady=8)

# Guess counter label
guess_label = tk.Label(root, text=" Attempts: 0 ", font=("Comic Sans MS", 12, "bold"), bg="#fff0f5", fg="#ff3399")
guess_label.pack(pady=8)

root.mainloop()
