# image from "https://www.freeiconspng.com/downloadimg/4988"
from tkinter import *
import random

COLOR = 'white'

root = Tk()
root.title("Password Manager")
root.geometry("600x400")
root.configure(background=COLOR)
root.grid_columnconfigure((0, 2), weight=2)

#------------------------------------------------------------------------------------
#functionality


#------------------------------------------------------------------------------------
#items
canvas = Canvas(root, width=256, bg=COLOR, height=256, highlightthickness=False)
image = PhotoImage(file="img.png")
canvas.create_image(128, 128, image=image)

Label1 = Label(root, text="Website")
Label1.configure(background=COLOR)
Label2 = Label(root, text="Email/Username")
Label2.configure(background=COLOR)
Label3 = Label(root, text="Password")
Label3.configure(background=COLOR)

Entry1 = Entry(root)
Entry1.configure(background=COLOR)
Entry2 = Entry(root)
Entry2.configure(background=COLOR)
Entry3 = Entry(root,width= 50)
Entry3.configure(background=COLOR)

Button1 = Button(text="Generate Password", background=COLOR, activebackground=COLOR)
Button2 = Button(text="Add",background=COLOR, height=1, activebackground='#a6f0c6')
#---------------------------------------------------------------------------------
#grids
canvas.grid(row=0, column=0,columnspan=3 , pady=10)
Label1.grid(row=1, column=0, pady=2.5)
Entry1.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(0, 50), pady=2.5)
Label2.grid(row=2, column=0, pady=2.5)
Entry2.grid(row=2, column=1, columnspan=2, sticky="ew", padx=(0, 50), pady=2.5)
Label3.grid(row=3, column=0, pady=2.5)
Entry3.grid(row=3, column=1, sticky="w", pady=2.5)
Button1.grid(row=3, column=2, sticky='e', padx=(0, 50), pady=2.5)
Button2.grid(row=4, column=1, columnspan=3, sticky='ew', padx=(0, 50), pady=2.5)


root.mainloop()
