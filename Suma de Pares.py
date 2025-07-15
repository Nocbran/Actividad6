print("Suma de pares")
suma = 0
n1 = int(input("Ingrese un numero entero: "))
for r in range(1,n1+1):
   if r % 2 == 0:
       print("Lista de nuemros: ",r)
       suma += r
print("La suma de numeros pares es: ",suma)



