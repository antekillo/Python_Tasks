from tkinter import*

root = Tk()

variable = int()
check = Checkbutton(root, text='пункт', variable=variable, onvalue=5, offvalue=0)
check.pack()

root.mainloop()
