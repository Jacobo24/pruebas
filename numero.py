import random
from random import randint
no = randint(1, 100)
print("Adivina el numero")
while True:
    n = int(input("Introduce un numero: "))
    if no < n:
        print("El numero es menor")
    elif no > n:
        print("El numero es mayor")
    else:
        print("Has acertado!")
        break




