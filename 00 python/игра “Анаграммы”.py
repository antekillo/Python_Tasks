import random
words = ['снижать', 'бяка', 'порт', 'горелка', 'кучерявый', 'пятиминутка', 'дожечь']
word = random.choice(words)
liters = str('')
correct = word
print(word)
while word:
    position = random.randrange(len(word))
    liters += word[position]
    word = word[:position] + word[(position + 1):]
print(liters)
while correct != words:
    answer = input("Ваш ответ: ")
    if correct == answer:
        print("U win!!!")
        break
    else:
        print("Попробуй ище ")