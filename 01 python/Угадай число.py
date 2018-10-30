import random
print("Привет, ты должен угадать число. Оно будет в диапазоне от 1 до 10")
nam = random.randint(1, 10)
print(nam)
answer = int(input())
while nam != answer:
    if answer > nam:
        print("Меньше")
    if answer < nam:
        print("Больше")
    if answer != nam:
        print("Try again")
        answer = int(input())
print("U win")