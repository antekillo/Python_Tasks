from tkinter import*
from tkinter import ttk
rood = Tk()
rood.geometry("600x600")
rood.title("Проект")
bttn = ttk.Button(rood, text="OK")
logo = PhotoImage(file="D:/Python/01 python/29Q.gif")
logo1 = Label(rood, image=logo)
logo1.pack()
bttn.pack()
rood.mainloop()