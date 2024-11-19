import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def start_game():
    start_button.grid_remove()
    logo_label.grid_remove()  # Hide the logo after starting the game
    
    for button in buttons:
        button.grid() 
    label.grid()  
    
    # Show Privacy Policy button at the bottom of the game
    privacy_button.grid(row=8, column=0, columnspan=3, pady=10)  
    exit_button.grid(row=9, column=0, columnspan=3, pady=(0, 20))  # Show Exit button at the bottom of the game

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="honeydew2")
            buttons[combo[1]].config(bg="honeydew2")
            buttons[combo[2]].config(bg="honeydew2")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            show_restart_button()  # Show Restart button when game ends
            return True  
    return False  

def check_tie():
    if all(button["text"] != "" for button in buttons):
        if not check_winner():  
            messagebox.showinfo("Tic-Tac-Toe", "Match Draw!")
            show_restart_button()  # Show Restart button when game ends

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        if current_player == "X":
            buttons[index].config(fg="cyan")
        else:
            buttons[index].config(fg="green yellow")
        if not check_winner():  
            check_tie()
            toggle_player()

def toggle_player():  
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def show_privacy_policy():
    privacy_policy_text = """AJ Srabon built the Tic-Tac-Toe game as a Free game. This SERVICE is provided by AJ Srabon at no cost and is intended for use as is.
    """
    messagebox.showinfo("Privacy Policy", privacy_policy_text)

def show_restart_button():
    restart_button.grid(row=7, column=0, columnspan=3, pady=10)  # Show Restart button

def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    
    # Reset all buttons
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    
    # Hide the Restart button
    restart_button.grid_remove()

def exit_game():
    root.quit()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="#B8860B")

logo_image = tk.PhotoImage(file="game_logo.png")

center_frame = tk.Frame(root, bg="#B8860B")
center_frame.pack(expand=True)

logo_label = tk.Label(center_frame, image=logo_image, bg="#B8860B")
logo_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))  

start_button = tk.Button(center_frame, text="Start Game", font=("normal", 20, "bold"), command=start_game)
start_button.grid(row=2, column=0, columnspan=3, pady=20)

buttons = [tk.Button(center_frame, text="", font=("normal", 25, "bold"), width=6, height=2, 
                     relief="solid", bd=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Initially hide the buttons (they will be shown after clicking "Start Game")
for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 3, column=i % 3)
    button.grid_remove()  

# Current player and label setup (initially hidden)
current_player = "X"
winner = False
label = tk.Label(center_frame, text=f"Player {current_player}'s turn", font=("normal", 16), bg="#B8860B")
label.grid(row=6, column=0, columnspan=3)
label.grid_remove()  

privacy_button = tk.Button(center_frame, text="Privacy Policy", font=("normal", 12), command=show_privacy_policy)

# Add Restart Button (initially hidden)
restart_button = tk.Button(center_frame, text="Restart", font=("normal", 16), command=restart_game)
restart_button.grid(row=7, column=0, columnspan=3, pady=10)
restart_button.grid_remove()

# Add Exit Button
exit_button = tk.Button(center_frame, text="Exit", font=("normal", 12), command=exit_game)
exit_button.grid(row=9, column=0, columnspan=3, pady=(0, 20))
exit_button.grid_remove()  # Hide it initially, it will be shown after starting the game

root.mainloop()
