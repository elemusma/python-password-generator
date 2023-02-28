from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    # [new_item for item in list]
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")
    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = input_website.get()
    user = input_user.get()
    password = input_pass.get()

    # print(len(website))

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title=website, message='You can\'t leave any empty fields')
    # messagebox.showinfo(title='Title', message='message')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {user}\nPassword: {password} \nIs it ok to save?')

        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f'{website} - {user} - {password}\n')
                input_website.delete(0, END)
                input_pass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, highlightthickness=0, bg='white')

pass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 112, image=pass_img)
canvas.grid(column=1, row=0)

#Labels
label_website = Label(text='Website:', bg='white', fg='black')
label_website.grid(column=0, row=1)
label_user = Label(text='Email/Username:', bg='white', fg='black')
label_user.grid(column=0, row=2)
label_pass = Label(text='Password:', bg='white', fg='black')
label_pass.grid(column=0, row=3)

#Input
input_website = Entry(width=39, bg='white', fg='black', highlightthickness=0)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_user = Entry(width=39, bg='white', fg='black', highlightthickness=0)
input_user.grid(column=1, row=2, columnspan=2)
input_user.insert(0, 'hello@brownsurfing.com')

input_pass = Entry(width=21, bg='white', fg='black', highlightthickness=0)
input_pass.grid(column=1, row=3)

#Button
button_pass = Button(text='Generate Password', bg='white', highlightthickness=0, command=generate_password)
button_pass.grid(column=2, row=3)

button_add = Button(text='Add', bg='white', highlightthickness=0, width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()