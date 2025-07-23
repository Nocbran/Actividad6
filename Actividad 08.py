def CalcFactorial (n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * CalcFactorial(n - 1)

def SumaNaturales (i,j):
    if i > j:
        return 0
    else:
        print(i)
        return i + SumaNaturales(i+1,j)

def Calcn_simNum (n):
    if n < 2:
        return n
    else:
        return Calcn_simNum(n-1)+Calcn_simNum(n-2)

def ContLetras (palabra,letra,n=0):
    if n >= len(palabra):
        return 0
    elif palabra[n].lower() == letra.lower():
        return  1 + ContLetras(palabra,letra,n+1)
    else:
        return ContLetras(palabra,letra,n+1)

'''def InverText():
    
def CalcPotencia():
    
def Salir(): '''

while True:
    print(f"\n________*******MENU*******________")
    print(f"1. Calcular el factorial de un numero")
    print(f"2. Suma de los primeros N numeros naturales")
    print(f"3. Calcular el n-esimo numero de fibonacci")
    print(f"4. Contar cuantas veces aprece una letra en una palabra")
    print(f"5. Invertir una cadena de texto")
    print(f"6. Calcular la potencia de un numero^exponente")
    print(f"7. Salir del programa")

    opcion = input(f"\nSeleccione una opcion: ")
    if opcion == '1':
        n = int(input("Ingrese el numero: "))
        print(f"El factorial es: {CalcFactorial(n)}")
        print(f"Desea regresar al menu?: ")

    elif opcion == '2':
        j = int(input("Ingrese el numero: "))
        Result = SumaNaturales(1,j)
        print(f"La suma de los numeros naturales es: {Result}")

    elif opcion == '3':
        n = int(input("Ingrese un numero: "))
        Fib = Calcn_simNum(n)
        print(f"El resultado fibonacci es: {Fib} ")

    elif opcion == '4':
        l = input(f"Ingrese la letra que sea conocer cuantas veces se repite: ")
        Nletras = ContLetras(palabra,letra,n=0)
        print(f"El numero de veces que se repite la letra seleccionada es: {ContLetras(l)}")
    '''elif opcion == '5':
        InverText()
    elif opcion == '6':
        CalcPotencia()
    elif opcion == '7':
        print("Asta pronto")
        break'''
