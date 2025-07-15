print("PIRAMIDE DE ASTERISCOS")
simbolo = "*"
n = int(input("Ingrese la altura del nivel de la piramide: "))
for i in range(1,n+1):
    aumento = n - i
    dibujo = (2*i)-1
    print(" "* aumento + simbolo * dibujo)


