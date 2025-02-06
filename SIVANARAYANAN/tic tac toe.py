import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x450")
        self.window.configure(bg="black")
        
        self.player1_name = simpledialog.askstring("Player 1", "Enter Player 1 name:")
        self.player1_coin = simpledialog.askstring("Choose Coin", f"{self.player1_name}, choose your coin (X/O):", initialvalue="X").upper()
        
        if self.player1_coin not in ["X", "O"]:
            self.player1_coin = "X"
        
        self.player2_name = simpledialog.askstring("Player 2", "Enter Player 2 name:")
        self.player2_coin = "O" if self.player1_coin == "X" else "X"
        
        self.board = [[None]*3 for _ in range(3)]
        self.current_player = self.player1_coin
        self.current_player_name = self.player1_name
        self.create_board()
        
        self.window.mainloop()
    
    def create_board(self):
        self.frame = tk.Frame(self.window, bg="black")
        self.frame.pack(expand=True)
        
        for i in range(3):
            for j in range(3):
                self.board[i][j] = tk.Button(
                    self.frame, text="", font=("Arial", 20, "bold"), width=5, height=2, 
                    command=lambda row=i, col=j: self.on_click(row, col),
                    bg="#D5DBDB", fg="#2C3E50", relief=tk.RAISED, borderwidth=10
                )
                self.board[i][j].grid(row=i, column=j, padx=5, pady=5)
        
    def on_click(self, row, col):
        if self.board[row][col]["text"] == "":
            self.board[row][col]["text"] = self.current_player
            self.board[row][col].config(fg="#FFD700" if self.current_player == self.player1_coin else "#00FFFF")
            if self.check_winner(row, col):
                self.display_winner_animation()
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = self.player2_coin if self.current_player == self.player1_coin else self.player1_coin
                self.current_player_name = self.player2_name if self.current_player_name == self.player1_name else self.player1_name
    
    def check_winner(self, row, col):
        b = self.board
        p = self.current_player
        
        return (
            all(b[row][i]["text"] == p for i in range(3)) or
            all(b[i][col]["text"] == p for i in range(3)) or
            all(b[i][i]["text"] == p for i in range(3)) or
            all(b[i][2-i]["text"] == p for i in range(3))
        )
    
    def is_draw(self):
        return all(self.board[i][j]["text"] != "" for i in range(3) for j in range(3))
    
    def display_winner_animation(self):
        winner_text = f"{self.current_player_name} wins! 🎉"
        winner_label = tk.Label(self.window, text=winner_text, font=("Arial", 18, "bold"), fg="#FFD700", bg="black")
        winner_label.pack()
        
        for _ in range(10):  # Popping effect with sparks
            winner_label.config(font=("Arial", random.randint(18, 28), "bold"))
            winner_label.config(fg=random.choice(["#FFD700", "#FF5733", "#00FFFF", "#28B463", "#E74C3C", "#9B59B6"]))
            self.window.update()
            time.sleep(0.2)
        
        messagebox.showinfo("Game Over", f"🎊 Congratulations {self.current_player_name}! You win! 🎊")
        self.window.after(2000, winner_label.destroy)
    
    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j]["text"] = ""
                self.board[i][j].config(bg="#D5DBDB")
        self.current_player = self.player1_coin
        self.current_player_name = self.player1_name

if __name__ == "__main__":
    TicTacToe()
