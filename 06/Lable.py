from tkinter import*

root = Tk()

lable = Label(bg='orange', fg='white', text='Hello world!', width=150, height=10, font='Courier 18')
lable.pack()


entry = Entry(root, width=30, bd=5, bg='black', fg='white', font='Courier 18', show="*")
entry.pack()


root.mainloop()

