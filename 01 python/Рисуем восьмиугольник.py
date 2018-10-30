
import turtle
t = turtle.Pen()
def octagon():
    for x in range(1, 9):
        t.forward(10)
        t.right(45)
octagon()
s = input("Для завершения программы нажми любую клавишу")