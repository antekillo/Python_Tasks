from tkinter import *
import random
print("Игральные кости")

def drop():
    text.delete(0.0, END)
    text.insert(END, str(random.randint(1, 6)))
def stop():
    print("Game over")
root = Tk()
text = Text(width=1, height=1)
text.pack()
buttonA = Button(root, text='Drop', command=drop)
buttonB = Button(root, text='Stop', command=stop)
buttonA.pack()
buttonB.pack()
root.mainloop()
