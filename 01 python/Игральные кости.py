import random
print("Игральные кости")
print("Для старта нажми 1, еслт хотите закончить игру нажмите 0")
game = int(input())
while game != 0:
    print("Чтобы бросить кубики нажми любою клавишу 1")
    game = int(input())
    num = random.randint(1, 6)
    print("Выпла цифра: {}" .format(num))
    0