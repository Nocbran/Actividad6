import random

print("MULTIPLO DE 3")


for listaNumeros in range(0,20):
    listaNumeros = random.randint(1, 100)
    if listaNumeros %3 == 0:
        print(listaNumeros)

