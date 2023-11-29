import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.player_score = 0
        self.computer_score = 0

        self.label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Player: 0  Computer: 0", font=("Helvetica", 12))
        self.score_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.config(text=f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\n{result}")
        self.score_label.config(text=f"Player: {self.player_score}  Computer: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
