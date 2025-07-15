print("Promedio de numeros positivos")
lista1 = []
promedio = 0
resultado = 0
suma = 0
numeros = 0
while True:
    numeros = int(input("Ingrese numeros positivos: "))
    if numeros <0:
        break
    lista1.append(numeros)
if len(lista1) > 0:
    resultado =sum(lista1)
    promedio = resultado / len(lista1)
    print("ingreso un numero negativo")
    print("El promedio de los numeros ingresados es: ",promedio)


