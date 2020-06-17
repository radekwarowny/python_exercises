# Gui input

from tkinter import *

root = Tk()

nameLabel = Label(root, text="What is your name? ")
nameLabel.pack()

name = Entry(root, width=50)
name.pack()

ageLabel = Label(root, text="How old are you? ")
ageLabel.pack()

age = Entry(root, width=50)
age.pack()


answer1 = Label(root, text="Hello, " + name.get() + ".")
answer1.pack()

answer2 = Label(root, text="So you are " + age.get() + ".")
answer2.pack()


root.mainloop()
