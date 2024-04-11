# %source /Users/Lukas.Deibel/code_repository/100_days_of_code/bin/activate

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

EMAIL = "deibel_lukas@gmx.de"
FILE = "day-29/password-manager-start/data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list +=[random.choice(numbers) for char in range(nr_numbers)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.delete(first=0, last=END)
    password_entry.insert(0,password)

    # Copy generated password directly to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def wipe_entries():
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    email_entry.insert(0,EMAIL)
    password_entry.delete(0,END)

def entry_invalid(*args):
    for arg in args:
        if len(arg) == 0:
            return TRUE
        
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        },
    }

    if entry_invalid(website, email, password):
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
        pass

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it ok to save?")
        if is_ok:
            try:
                with open(file=FILE, mode="r") as file:
                    # json.dump(new_data, file, indent=4)
                    data = json.load(file)

            except FileNotFoundError:
                with open(file=FILE, mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                
                with open(file=FILE, mode="w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                wipe_entries()

def search():
    website = website_entry.get()
    try:
        with open(file=FILE, mode="r") as file:
            # json.dump(new_data, file, indent=4)
            data = json.load(file)
            email = data[website]["email"]
            password = data[website]["password"]

    except FileNotFoundError:
        messagebox.showerror(title=website, message=f"No File found")
    
    except KeyError:
        messagebox.showerror(title=website, message=f"No entries for {website}")

    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="day-29/password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1,row=0)

# Label
website_label = Label(text="Website")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.insert(0,EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password, width=10)
password_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", command=save, width=32)
add_button.grid(column=1, row=4, columnspan=2)

# Search Button
search_button = Button(text="search", command=search, width=10)
search_button.grid(column=2, row=1)

window.mainloop()