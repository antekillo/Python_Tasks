import random
print("ПРИВЕДЕНИЯ")
dor = True
sco = 0
while dor:
    ghost = random.randint(1, 3)
    print("Выбире дверь: \n")
    chose = int(input("Выбирете 1, 2 или 3 дверь"))
    if ghost == chose:
        print("АААААААА. Здесь приведение")
        print("Game over")
        dor = False
    else:
        print("Здесь никого нет. Какая же дверь следуйщая")
        sco = sco + 1
print("Твой счет: {}" .format(sco))