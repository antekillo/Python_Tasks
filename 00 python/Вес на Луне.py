weigh = input("Сколько ты весишь? ")
weigh.isdigit()
if weigh.isdigit():
    weigh = int(weigh)
    weigh = weigh/6
    print("Твой вес на луне: {}" .format(weigh))
else:
    print("Я тебя не понимаю")

