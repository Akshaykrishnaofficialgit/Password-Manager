from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
password_list=[]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def make_a_pwd():
    password_list.clear()
    letter_range=random.randint(2,5)
    number_range=random.randint(2,5)
    symbol_range=random.randint(1,3)
    for i in range(letter_range):
        password_list.append(random.choice(letters))
    for i in range(number_range):
        password_list.append(random.choice(numbers))
    for i in range(symbol_range):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    pwd_string="".join(password_list)
    pyperclip.copy(pwd_string)
    return pwd_string
def auto_pwd():
    entry=messagebox.askyesno(message="Do you want to Generate a random password?")
    result=make_a_pwd()
    current_pwd=password_entry.get()
    if entry and current_pwd:
        password_entry.delete(0,END)
        password_entry.insert(END,result)
    else:
        password_entry.insert(END,result)


def auto_search():
    pass
    input_website=website_entry.get()
    try:
        with open("Data.json","r") as data:
            full_data=json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File does not Exist!")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Error decoding JSON file!")
    else:
        if input_website in full_data:
            mail=full_data[input_website]["Email"]
            pwd=full_data[input_website]["Password"]
            if_yes=messagebox.askyesno(title=input_website,message=f"Email: {mail}\nPassword: {pwd}")
            if if_yes:
                email_entry.delete(0,END)
                email_entry.insert(0,mail)
                password_entry.insert(0,pwd)
                pyperclip.copy(pwd)
        else:
            messagebox.showinfo(title="Not found",message="The password for this website is not saved previously!")




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    Email=email_entry.get()
    Password=password_entry.get()
    new_data={website:{
        "Email":Email,
        "Password":Password
    }}
    if len(website)==0 or len(Password)==0:
        messagebox.showwarning(title="Error",message="Cannot leave the fields empty!")
    else:
        try:
            with open("Data.json","r") as data_file:
                #reading old data
                data=json.load(data_file)
                #updating old data with new data
        except FileNotFoundError:
            with open("Data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("Data.json","w") as data_file:
                #saving updated data
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="black")

# Configure canvas for logo
canvas = Canvas(height=200, width=200, bg="black", highlightthickness=0)
lock_image = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1, columnspan=2, pady=(0, 20))

# Configure Labels
label_font = ('Arial', 12, 'bold')
label_fg = "white"
label_bg = "black"

website = Label(text="Website:", font=label_font, fg=label_fg, bg=label_bg)
website.grid(row=1, column=0, sticky="e", padx=(0, 10))

email = Label(text="Email/Username:", font=label_font, fg=label_fg, bg=label_bg)
email.grid(row=2, column=0, sticky="e", padx=(0, 10))

password = Label(text="Password:", font=label_font, fg=label_fg, bg=label_bg)
password.grid(row=3, column=0, sticky="e", padx=(0, 10))

# Configure Entries
entry_font = ('Arial', 10,'bold')
entry_bg = "white"
entry_fg = "black"

website_entry = Entry(width=36, bg=entry_bg, fg=entry_fg, borderwidth=1, font=entry_font)
website_entry.grid(row=1, column=1, columnspan=2, pady=(0, 10))
website_entry.focus()

email_entry = Entry(width=36, bg=entry_bg, fg=entry_fg, borderwidth=1, font=entry_font)
email_entry.grid(row=2, column=1, columnspan=2, pady=(0, 10))
email_entry.insert(0, "akshaysasidhar5@gmail.com")

password_entry = Entry(width=36, bg=entry_bg, fg=entry_fg, borderwidth=1, font=entry_font)
password_entry.grid(row=3, column=1, columnspan=2, pady=(0, 10))

# Configure Buttons
button_font = ('Arial', 12, 'bold')
button_bg = "black"
button_fg = "white"

generate_button = Button(text="Generate Password", width=20, command=auto_pwd, font=button_font, bg=button_bg, fg=button_fg)
generate_button.grid(row=3, column=3, columnspan=2, padx=(10, 0),pady=(0,10))

add_button = Button(text="Add", width=30, command=save, font=button_font, bg=button_bg, fg=button_fg)
add_button.grid(row=4, column=1, columnspan=2, padx=(10, 0),pady=(0,10))
add_button.config(fg="#48CFCB")

search_button = Button(text="Search Password", width=20, command=auto_search, font=button_font, bg=button_bg, fg=button_fg)
search_button.grid(row=1, column=3, columnspan=2, padx=(10, 0))


window.mainloop()









