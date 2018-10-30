
import random
orel = 0
rec = 0
for n in range(0,50):
    a = random.randint(0, 1)
    if a == 0:
        orel = orel+1
    else:
        rec = rec+1
print("Орел выпал {} раз. Решка вырала {} раз " .format(orel, rec))
