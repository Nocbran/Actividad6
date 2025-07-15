import random

print("JUEGO DE ADIVINANZAS")
n = int(input("Ingrese un numero: "))
ale = random.randint(1,100)
if n == ale:
    print("Numero correcto")
else:
    while n < ale or n > ale:
        print("Numero por debajo, introduzca un valor mas alto")
        n = int(input("Ingrese un numero: "))
        if n > ale:
           print("Numero por encima, introduzca un valor mas bajo")
           n = int(input("Ingrese un numero: "))
