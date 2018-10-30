from tkinter import*
from tkinter import ttk
import random

nam = random.randint(1, 10)
print(nam)
root = Tk()
root.geometry("1000x1000")
lb = Label(text='''Привет, давай поиграем в игру. Я загадывю число от 1 до 10 и ты должен отгадать его.

Введи свое предположение''', font="Arial")
lb.pack()
e = Entry()
e.pack()

def get():
    s = int(e.get())
    if s > nam:
        lable = Label(text="Число {} не верное, загаданное число меньше" .format(s))
        lable.pack()
        e.delete(0, END)
    if s < nam:
        lable = Label(text="Число {} не верное, загаданное число больше".format(s))
        lable.pack()
        e.delete(0, END)
    if s == nam:
        lable = Label(text="Урааа, ты отгадал это число. Правильный ответ {}".format(s))
        lable.pack()



b_get = ttk.Button(text="Проверить число", command=get)
b_get.pack()
root.mainloop()