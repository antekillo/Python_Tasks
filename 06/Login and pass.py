from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry('600x600')
lb1 = Label(root, text='Для входа в систему, зарагестрируйтесь!')
lb1.pack()
lb2 = Label(root, text='Введите логин:')
lb2.pack()
entr1 = Entry()
entr1.pack()
login = entr1.get()
lb3 = Label(root, text='Введите пароль:')
lb3.pack()
entr2 = Entry(root, show='*')
entr2.pack()
lb4 = Label(root, text='Повторите пароль:')
lb4.pack()
entr3 = Entry(root, show='*')
entr3.pack()
def regi():
    messagebox.showinfo("Reg", '''Login: {} \n Pass: {}''' .format(entr1.get(), entr2.get()))

btn = Button(root, text='Зарегестрироваться!', command=regi)
btn.pack()


root.mainloop()