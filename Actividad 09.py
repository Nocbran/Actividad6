Clientes = {}
def Reg_Clientes (n,cont=1):
    if cont > n:
        return  0
    print(f"\nCliente #{cont}")
    codigo = int(input("Ingrese el codigo del cliente: "))
    nombre = input("Ingrese el nombre del cliente: ")

    while True:
        CantDestinos = int(input("Cuantos destinos desea registrar: "))
        if 1 <= CantDestinos <=3:
            break
        else:
            print("El maximo registro de destinos es 3!")

    destinos = []
    for i in range(CantDestinos):
        destino = input(f"Destino {i+1}: ").strip()
        destinos.append(destino)

    clientes[codigo] = {
        "Nombre": nombre,
        "destino" : destinos
    }

    Reg_Clientes(n, cont + 1)




print("Bienvenido")
n = int(print(f"\nCuantos clientes desea registrar: "))
