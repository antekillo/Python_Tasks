from tkinter import*

root = Tk()

text = Text(root, width=7, height=7, bd=6, bg='white', fg='blue', font='Arial 16')
text.insert(0.0, 'Hello world!')
text.delete("1.0", "1.5")
text.pack()

root.mainloop()
