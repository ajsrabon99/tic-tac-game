import tkinter as tk
from tkinter import messagebox
import random  # For AI to choose moves

def start_game():
    start_button.grid_remove()
    logo_label.grid_remove()  # Hide the logo after starting the game
    
    # Show the game mode options
    play_with_ai_button.grid(row=2, column=0, columnspan=3, pady=(10, 10))
    play_with_friends_button.grid(row=3, column=0, columnspan=3, pady=(10, 10))
    privacy_button.grid(row=4, column=0, columnspan=3, pady=10)  # Show Privacy button here

def select_mode(mode):
    global ai_mode
    ai_mode = (mode == "AI")
    
    # Hide mode selection buttons
    play_with_ai_button.grid_remove()
    play_with_friends_button.grid_remove()
    privacy_button.grid_remove()
    
    # Show game elements
    for button in buttons:
        button.grid()
    label.grid()
    
    # Show bottom buttons
    exit_button.grid(row=9, column=0, columnspan=3, pady=(0, 20))
    
    toggle_player()  # Start the game

def back_to_mode_selection():
    # Reset the game board
    restart_game()
    
    # Hide game elements
    for button in buttons:
        button.grid_remove()
    label.grid_remove()
    restart_button.grid_remove()
    back_button.grid_remove()
    
    # Show mode selection buttons
    play_with_ai_button.grid(row=2, column=0, columnspan=3, pady=(10, 10))
    play_with_friends_button.grid(row=3, column=0, columnspan=3, pady=(10, 10))
    privacy_button.grid(row=4, column=0, columnspan=3, pady=10)

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="honeydew2")
            buttons[combo[1]].config(bg="honeydew2")
            buttons[combo[2]].config(bg="honeydew2")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            show_end_buttons()  # Show Restart and Back buttons
            return True  
    return False  

def check_tie():
    if all(button["text"] != "" for button in buttons):
        if not check_winner():  
            messagebox.showinfo("Tic-Tac-Toe", "Match Draw!")
            show_end_buttons()  # Show Restart and Back buttons

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
            if ai_mode and current_player == "O" and not winner:  # AI's turn
                ai_move()

def ai_move():
    empty_indices = [i for i, button in enumerate(buttons) if button["text"] == ""]
    if empty_indices:
        ai_choice = random.choice(empty_indices)  # Choose a random empty spot
        buttons[ai_choice]["text"] = current_player
        buttons[ai_choice].config(fg="green yellow")
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

def show_end_buttons():
    restart_button.grid(row=7, column=0, columnspan=3, pady=10)  # Show Restart button
    back_button.grid(row=8, column=0, columnspan=3, pady=10)  # Show Back button

def restart_game():
    global current_player, winner
    current_player = "X"
    winner = False
    label.config(text=f"Player {current_player}'s turn")
    
    # Reset all buttons
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    
    # Hide the Restart and Back buttons
    restart_button.grid_remove()
    back_button.grid_remove()

def exit_game():
    root.quit()

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")  # Set the window size
root.config(bg="#B8860B")

# Load logo image
logo_image = tk.PhotoImage(file="game_logo.png")

center_frame = tk.Frame(root, bg="#B8860B")
center_frame.pack(expand=True)

logo_label = tk.Label(center_frame, image=logo_image, bg="#B8860B")
logo_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))  

start_button = tk.Button(center_frame, text="Start Game", font=("normal", 20, "bold"), bg="red", fg="white", command=start_game)
start_button.grid(row=2, column=0, columnspan=3, pady=20)

play_with_ai_button = tk.Button(center_frame, text="Play with AI", font=("normal", 16), bg="sky blue", command=lambda: select_mode("AI"))
play_with_friends_button = tk.Button(center_frame, text="Play with Friends", font=("normal", 16), bg="light pink", command=lambda: select_mode("Friends"))
privacy_button = tk.Button(center_frame, text="Privacy Policy", font=("normal", 12), command=show_privacy_policy)

buttons = [tk.Button(center_frame, text="", font=("normal", 25, "bold"), width=6, height=2, 
                     relief="solid", bd=2, command=lambda i=i: button_click(i)) for i in range(9)]

# Initially hide the buttons (they will be shown after selecting a mode)
for i, button in enumerate(buttons):
    button.grid(row=(i // 3) + 3, column=i % 3)
    button.grid_remove()  

# Current player and label setup (initially hidden)
current_player = "X"
winner = False
ai_mode = False  # Whether AI is enabled or not
label = tk.Label(center_frame, text=f"Player {current_player}'s turn", font=("normal", 16), bg="#B8860B")
label.grid(row=6, column=0, columnspan=3)
label.grid_remove()  

# Add Restart Button (initially hidden)
restart_button = tk.Button(center_frame, text="Restart", font=("normal", 16), bg="blue", fg="white", command=restart_game)
restart_button.grid(row=7, column=0, columnspan=3, pady=10)
restart_button.grid_remove()

# Add Back Button (initially hidden)
back_button = tk.Button(center_frame, text="Back", font=("normal", 16), bg="light coral", fg="black", command=back_to_mode_selection)
back_button.grid(row=8, column=0, columnspan=3, pady=10)
back_button.grid_remove()

# Add Exit Button
exit_button = tk.Button(center_frame, text="Exit", font=("normal", 12), bg="red", fg="white", command=exit_game)
exit_button.grid(row=9, column=0, columnspan=3, pady=(0, 20))
exit_button.grid_remove()  # Hide it initially, it will be shown after starting the game


root.mainloop()
