from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symb in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]


    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Incomplete Fields",message="Please don't leave blank fields !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Following are the details entered: \nEmail: {email}"
                            f"\n Password: {password} \n Is it ok ?")

        if is_ok:
            # Save data to a text file
            with open("data.txt", "a") as file:
                file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
                # Clear entry fields
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2, sticky='EW')
website_entry.focus()

email_label = Label(text="Username/Email:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2, sticky='EW')
email_entry.insert(0,'gk@gmail.com')

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3, sticky='EW')

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2,row=3, sticky='EW')

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky='EW')

window.mainloop()
