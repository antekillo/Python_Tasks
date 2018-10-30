from tkinter import*

root = Tk()

entry = Listbox(root, bd=3, bg='red', fg='black', font='Arial 12')
entry.insert(END, 'Hello')
entry.insert(END, 'Hello')
entry.insert(END, 'Hello')

entry.insert(END, 'World')
entry.insert(END, 'World')
entry.insert(END, 'World')

entry.insert(END, 'ITGENIO')
entry.insert(END, 'ITGENIO')
entry.insert(END, 'ITGENIO')

entry.pack()
root.mainloop()
