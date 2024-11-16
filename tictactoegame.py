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
    privacy_button.grid(row=7, column=0, columnspan=3, pady=10)  

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="honeydew2")
            buttons[combo[1]].config(bg="honeydew2")
            buttons[combo[2]].config(bg="honeydew2")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return True  
    return False  

def check_tie():
    if all(button["text"] != "" for button in buttons):
        if not check_winner():  
            messagebox.showinfo("Tic-Tac-Toe", "Match Draw!")
            root.quit()

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
    privacy_policy_text = """Privacy Policy
AJ Srabon built the Tic-Tac-Toe game as a Free game. This SERVICE is provided by AJ Srabon at no cost and is intended for use as is.

This page is used to inform visitors regarding my policies with the collection, use, and disclosure of Personal Information if anyone decided to use my Service.

If you choose to use my Service, then you agree to the collection and use of information in relation to this policy. The Personal Information that I collect is used for providing and improving the Service. I will not use or share your information with anyone except as described in this Privacy Policy.

The terms used in this Privacy Policy have the same meanings as in our Terms and Conditions, which is accessible at Tic-Tac-Toe unless otherwise defined in this Privacy Policy.

Information Collection and Use

For a better experience, while using our Service, I may require you to provide us with certain personally identifiable information. The information that I request will be retained on your device and is not collected by me in any way.

The game does use third party services that may collect information used to identify you.

Link to privacy policy of third party service providers used by the game

Google Play Services
Log Data

I want to inform you that whenever you use my Service, in a case of an error in the game I collect data and information (through third party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (“IP”) address, device name, operating system version, the configuration of the game when utilizing my Service, the time and date of your use of the Service, and other statistics.

Cookies

Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.

This Service does not use these “cookies” explicitly. However, the game may use third party code and libraries that use “cookies” to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies, you may not be able to use some portions of this Service.

Service Providers

I may employ third-party companies and individuals due to the following reasons:

To facilitate our Service;
To provide the Service on our behalf;
To perform Service-related services; or
To assist us in analyzing how our Service is used.
I want to inform users of this Service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However, they are obligated not to disclose or use the information for any other purpose.

Security

I value your trust in providing us your Personal Information, thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet, or method of electronic storage is 100% secure and reliable, and I cannot guarantee its absolute security.

Links to Other Sites

This Service may contain links to other sites. If you click on a third-party link, you will be directed to that site. Note that these external sites are not operated by me. Therefore, I strongly advise you to review the Privacy Policy of these websites. I have no control over and assume no responsibility for the content, privacy policies, or practices of any third-party sites or services.

Children’s Privacy

These Services do not address anyone under the age of 13. I do not knowingly collect personally identifiable information from children under 13. In the case I discover that a child under 13 has provided me with personal information, I immediately delete this from our servers. If you are a parent or guardian and you are aware that your child has provided us with personal information, please contact me so that I will be able to do necessary actions.

Changes to This Privacy Policy

I may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes. I will notify you of any changes by posting the new Privacy Policy on this page. These changes are effective immediately after they are posted on this page.

Contact Us

If you have any questions or suggestions about my Privacy Policy, do not hesitate to contact me at ashrafuzzamansrabon@gmail.com
"""

    messagebox.showinfo("Privacy Policy", privacy_policy_text)

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

root.mainloop()
