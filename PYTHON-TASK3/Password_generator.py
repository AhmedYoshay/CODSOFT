import tkinter as tk
import random

def Password_Generator():
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                  'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                  'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', 
                  "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[',
                  '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    try:
        length = int(length_entry.get())  # Validation
        if length <= 0:
            raise ValueError
    except ValueError:
        password_display.config(state=tk.NORMAL)
        password_display.delete("1.0", tk.END)
        password_display.insert(tk.END, "Please enter a valid positive integer for password length.")
        password_display.config(state=tk.DISABLED)
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(state=tk.NORMAL)
    password_display.delete("1.0", tk.END)
    password_display.insert(tk.END, password)
    password_display.config(state=tk.DISABLED)

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="blue")
font = ("Arial", 16)

# labels and entry widgets

length_label = tk.Label(root, text="Enter the length of password you want:", font=font, bg="blue", fg="white")
length_label.pack()
length_entry = tk.Entry(root, font=font)
length_entry.pack()

# Generate button

generate_button = tk.Button(root, text="Generate Password", font=font, command=Password_Generator)
generate_button.pack(pady=10) 

password_label = tk.Label(root, text="Your Password:", font=font, bg="blue", fg="white")
password_label.pack()

# Password display

password_display = tk.Text(root, font=font, bg="white", fg="black", width=30, height=3, borderwidth=2, relief="solid")
password_display.pack()

root.geometry("400x280")  
root.mainloop()
