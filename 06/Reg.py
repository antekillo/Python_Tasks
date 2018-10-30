from tkinter import *
from tkinter import messagebox
import pickle


root = Tk()
root.geometry("600x600")
root.title("Войти в систему")

def registration ():
    lb1 = Label(root, text='Для входа - зарегестрируйтесь!')
    text_log = Label(root, text="Введите логин:")
    reg_login = Entry()
    text_password = Label(root, text="Введите пароль:")
    reg_password = Entry()
    text_password2 = Label(root, text="Повторите пароль:")
    reg_password2 = Entry(show="*")
    btn = Button(root, text="Зарегестрировать!", command=lambda: save())
    lb1.pack()
    text_log.pack()
    reg_login.pack()
    text_password.pack()
    reg_password.pack()
    text_password2.pack()
    reg_password2.pack()
    btn.pack()

    def save():
        login_pass_save = {}
        login_pass_save[reg_login.get()] = reg_password.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

def login():
    text_log = Label(text='Теперь вы можете зайти в систему!')
    text_enter_login = Label(text='Введите ваш логин!')
    enter_login = Entry()
    text_enter_password = Label(text='Введите ваш пароль!')
    enter_password = Entry(show="*")
    btn2 = Button (text='Войти', command=lambda: log())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_password.pack()
    enter_password.pack()
    btn2.pack()

    def log():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен", "Hellow world")
        else:
            messagebox.showerror("Ошибка", "Not work")





registration()

root.mainloop()