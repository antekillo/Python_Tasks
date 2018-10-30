from tkinter import*
import random


root = Tk()

root.title('Палочки')
root.geometry('600x600')
count = 20

lb1 = Label(text='Введите число от 1 до 3')
entr_count = Entry()
lb1.pack()
entr_count.pack()

lb2 = Label(text=count*'|', font="Arial 24")
lb2.pack()
lb3 = Label(text=count, font="Arial 24")
lb3.pack()
btn2 = Button(text='Твой ход', command=lambda: play())
btn2.pack()

def play():
    if int(entr_count.get()) in [1, 2, 3]:
        global count
        count = count - int(entr_count.get())
        lb2.config(text=count*"|")
        lb3.config(text=count)

    else:
        lb3.config(text='Ошибка!')

    if count == 1:
        lb3.config(text="Ты выйграл")
    entr_count.delete(0, END)
    lb1.config(text='Ход компьютреа')
    root.after(2000, lambda: comp())


def comp():

    global count
    count = count - random.randint(1, 3)
    lb2.config(text=count * "|")
    lb3.config(text=count)
    if count == 1:
        lb3.config(text="Я выйграл")
    lb1.config(text='Введите число от 1 до 3')


root.mainloop()


