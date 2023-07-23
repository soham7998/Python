import datetime
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("620x780")
window.title("Age Calculator")

name_label = tk.Label(text="Name")
name_label.grid(column=0, row=1)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=2)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=3)

date_label = tk.Label(text="Day")
date_label.grid(column=0, row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)

monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)

def getinput():
    name = nameEntry.get()
    monkey = Person(name, int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get()))
    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)

    answer = f"Hey, {monkey.name}!! You are {monkey.age()} years old."
    textArea.insert(tk.END, answer)

button = tk.Button(window, text="Calculate Age", command=getinput, bg="Red")
button.grid(column=1, row=5)

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.birthdate = datetime.date(year, month, day)

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

# Use an image in the GUI
# image = Image.open('./python/tkinter/app_image.png')
# image.thumbnail((512, 512), Image.ANTIALIAS)
# photo = ImageTk.PhotoImage(image)
# label_image = tk.Label(image=photo)
# label_image.grid(column=1, row=0)

window.mainloop()
