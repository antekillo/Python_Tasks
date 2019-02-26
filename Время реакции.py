from tkinter import *
import time
import random

root = Tk()
root.geometry("500x500")
root.title('Время реакции')
canvas = Canvas(root, width=500, height=500)
canvas.delete("all")

list=[]
y=20
count=0


def main():
    global ball
    ball = canvas.create_oval(225, 225, 275, 275, fill="black")
    root.after(random.randint(3000, 10000), set_time)

def set_time():
    global start_time
    start_time = time.time()
    canvas.itemconfig(ball, fill="green")

def temer(event):
    global start_time, y, list, count

    if count<3:
        count+=1
        root.after(500, lambda: main())
    else:
        canvas.delete("all")
        total=round(float(sum(list)) / len(list), 3)
        canvas.create_text(225, 225, font="Arial 14", text="Твое среднее время реакции {}".format(total))
        return


    sec = round(time.time() - start_time, 3)
    if sec<1:
        list.append(sec)
        print("--- %s seconds ---" %sec)
        canvas.delete(ball)
        canvas.create_text(40, y, font="Arial 14", text=sec)
        y += 20

    else:
        list.append(1)
        canvas.delete(ball)
        print("--- 1 seconds ---")
        canvas.create_text(40, y, font="Arial 14", text=1)
        y += 20

canvas.bind_all('<Button-1>', temer)
canvas.pack()

main()
root.mainloop()












