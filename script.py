import random
from tkinter import *

root = Tk()
root.title('Random Password Generator')

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for the Tk root window
x = (screen_width - 450) // 2  # 450 is the width of the window
y = (screen_height - 450) // 2  # 450 is the height of the window

root.geometry('450x450+{}+{}'.format(x, y))  # Set the window to be centered

# Colors
bg_color = '#f0f0f0'  # Light gray background
fg_color = '#333333'  # Dark gray foreground
button_bg_color = 'blue'  # Green button background
button_fg_color = 'white'  # White button foreground

root.configure(bg=bg_color)

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='

characters = alpha_lower + alpha_upper + numbers + symbols

# Title
Label(root, text="Welcome to Random Password Generator", font=('Arial bold', 16), bg=bg_color, fg=fg_color).place(relx=0.5, rely=0.12, anchor=CENTER)

# Number of characters label and entry
Label(root, text="Number of characters", font=('Arial bold', 12), bg=bg_color, fg=fg_color).place(relx=0.5, rely=0.27, anchor=CENTER)
character_length = Entry(root, font="Arial 14")
character_length.place(relx=0.5, rely=0.32, anchor=CENTER)

def generate_password():
    length = character_length.get()
    if length.isdigit() and int(length) >= 4:
        password = [
            random.choice(alpha_lower),
            random.choice(alpha_upper),
            random.choice(numbers),
            random.choice(symbols)
        ]
        
        remaining_length = int(length) - 4
        password += random.sample(characters, remaining_length)
        random.shuffle(password)
        password = "".join(password)
        
        label_password.config(text='Generated Password: ' + password)
    else:
        label_password.config(text='Please enter a valid number greater than or equal to 4')

Button(root, text="Generate Password", command=generate_password, font=('Arial bold', 12), bg=button_bg_color, fg=button_fg_color).place(relx=0.5, rely=0.4, anchor=CENTER)
label_password = Label(root, font=('Arial bold', 12), bg=bg_color, fg=fg_color)
label_password.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
