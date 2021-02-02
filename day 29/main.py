# image from "https://www.freeiconspng.com/downloadimg/4988"
from tkinter import *
from tkinter import messagebox
import random
import string
import json

letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = list(string.punctuation)

COLOR = 'white'

root = Tk()
root.title("Password Manager")
root.geometry("600x400")
root.configure(background=COLOR)
root.grid_columnconfigure((0, 2), weight=2)


# -----------------------------functionality-----------------------------
def generate_password():
    letters_temp = random.choices(letters, k=8)
    digits_temp = random.choices(digits, k=3)
    punctuation_temp = random.choices(punctuation, k=3)
    stack = letters_temp + digits_temp + punctuation_temp
    random.shuffle(stack)
    return "".join(stack)


def generate_button():
    Entry3.delete(0, "end")
    Entry3.insert(0, generate_password())


def search_info():
    website = Entry1.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Missing Data File.")
    else:
        if website in data:
            messagebox.showinfo("Info", f'Email: {data[website]["email"]}\nPassword: {data[website]["password"]}')
        else:
            messagebox.showerror("Error", "No results match your search criteria.")


def save_to_json():
    website = Entry1.get()
    email = Entry2.get()
    password = Entry3.get()
    file_document = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website != '' and email != '' and password != "":
        ask = messagebox.askquestion("Password Manager", f"Email: {email}\nPassword: {password}\nIs this ok?")
        if ask == "yes":
            Button2.configure(background=COLOR)
            try:
                with open("data.json", 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(file_document, file, indent=4)
            else:
                data.update(file_document)
                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                Entry1.delete(0, "end")
                Entry2.delete(0, "end")
                Entry3.delete(0, "end")
        else:
            Button2.configure(background=COLOR)
    else:
        messagebox.showerror("Error", "Fill in all required entry fields.")


# -----------------------------items-----------------------------
canvas = Canvas(root, width=256, bg=COLOR, height=256, highlightthickness=False)
image = PhotoImage(file="img.png")
canvas.create_image(128, 128, image=image)

Label1 = Label(root, text="Website")
Label1.configure(background=COLOR)
Label2 = Label(root, text="Email/Username")
Label2.configure(background=COLOR)
Label3 = Label(root, text="Password")
Label3.configure(background=COLOR)

Entry1 = Entry(root, width=50)
Entry1.configure(background=COLOR)
Entry2 = Entry(root)
Entry2.configure(background=COLOR)
Entry3 = Entry(root, width=50)
Entry3.configure(background=COLOR)

Button1 = Button(text="Generate Password",
                 background=COLOR,
                 activebackground=COLOR,
                 width=17,
                 command=generate_button)
Button2 = Button(text="Add",
                 background=COLOR,
                 height=1,
                 activebackground='#a6f0c6',
                 command=save_to_json)
Button3 = Button(text="Search",
                 width=17,
                 background=COLOR,
                 activebackground='#a6f0c6',
                 command=search_info)

# -----------------------------grids-----------------------------
canvas.grid(row=0, column=0, columnspan=3, pady=10)
Label1.grid(row=1, column=0, pady=2.5)
Entry1.grid(row=1, column=1, sticky="ew", pady=2.5)
Label2.grid(row=2, column=0, pady=2.5)
Entry2.grid(row=2, column=1, columnspan=2, sticky="ew", padx=(0, 50), pady=2.5)
Label3.grid(row=3, column=0, pady=2.5)
Entry3.grid(row=3, column=1, sticky="w", pady=2.5)
Button1.grid(row=3, column=2, sticky='e', padx=(0, 50), pady=2.5)
Button2.grid(row=4, column=1, columnspan=3, sticky='ew', padx=(0, 50), pady=2.5)
Button3.grid(row=1, column=2, sticky='e', padx=(0, 50), pady=2.5)

root.mainloop()
