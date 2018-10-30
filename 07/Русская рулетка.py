import random
count = 0
bul = [0, 0, 1, 0, 0, 0]
live = True

while live:
    print('Чтобы стрельнуть, нажми Enter')
    input()
    num = len(bul)
    if bul[random.randint(0, num-1)] == 0:
        print('Стреляй еще')
    else:
        print('Ты умер(')
        live = False

