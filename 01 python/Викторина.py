from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("600x600")
root.title('Викторина')

def que_one():
    question = Label(root, text="Висит груща нельзя скушать?")
    answer = Entry()
    btn = Button(root, text="Ответить",  command=lambda: game1(que_tow()))
    question.pack()
    answer.pack()
    btn.pack()
    def game1(que_tow):
        if answer.get() == "Лампочка":
            que_tow()
        else:
            messagebox.showerror("Ошибка", "Попробуй еще! ")

def que_tow():
    question_2 = Label(root, texr="Зимой и летом одним цветом")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить")
    question_2.pack()
    answer_2.pack()
    btn_2.pack()


que_one()
root.mainloop()
