playtext = input("Введите слово")
key = int(input("Введите сдвиг"))

def caser_encrypt(playtext, key):

    s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    cip = ''
    for latter in playtext:
        new_s = (s.find(latter.lower()) + key) % len(s)
        cip = cip + s[new_s]

    print(cip)
    decaser_encrypt(cip, key)


def decaser_encrypt(cip, key):

    s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    decip = ''
    for latter in cip:
        new_s = (s.find(latter.lower()) - key) % len(s)
        decip = decip + s[new_s]


    print(decip)

caser_encrypt(playtext, key)

