import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.config(background="#8d493e")
board, player, active = [" "] * 9, "X", True
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def click(i):
    global player, active
    if board[i] != " " or not active: return
    board[i] = player
    buttons[i].config(text=player)
    if any(board[a]==board[b]==board[c]==player for a,b,c in wins):
        messagebox.showinfo("Game Over", f"{player} Wins!"); active = False
    elif " " not in board:
        messagebox.showinfo("Game Over", "It's a draw! Well played both!"); active = False
    else:
        player = "O" if player == "X" else "X"
        label.config(text=f"Player {player}'s Turn")

def reset():
    global board, player, active
    board, player, active = [" "] * 9, "X", True
    label.config(text="Player X's Turn")
    for btn in buttons: btn.config(text=" ")

buttons = [tk.Button(root, text=" ", font=("Arial", 20), fg="#bf004a", width=5, height=2, bg="white", command=lambda i=i: click(i)) for i in range(9)]
for i, btn in enumerate(buttons): btn.grid(row=(i//3)+1, column=i%3)


label = tk.Label(root, text="Player X's Turn", bg="#8d493e", fg="white", font="TimesNewRoman")
label.grid(row=0, column=0, columnspan=3, sticky='ew')
tk.Button(root, text="Restart", bg="#8d493e", fg="white", font="TimesNewRoman", command=reset).grid(row=4, column=0, columnspan=3)

root.mainloop() 
