import random

numrand=random.randint(0,5)
num=-1
while num != numrand:
    num=int(input("Que número estoy pensando?: "))

print("Adivinaste era el número que pensaba %d" % (int(num)))