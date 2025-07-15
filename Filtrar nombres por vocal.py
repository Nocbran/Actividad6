print("FILTRADO DE NOMBRES POR VOCAL")
print("Debe ingresar 10 nombres")
lista = []

for i in range(10):
    nombres = input("Ingreso de nombres: ")
    lista.append(nombres)
    vocales = "aeiou"

    for nombres in lista:
        primerletra = nombres[0]
        if primerletra in vocales:
             print(nombres)





