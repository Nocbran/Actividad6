productos ={}
print("BIENVENIDO AL INVENTARIO DE ROPA")
cantidad = int(input(f"\nIndique la cantidad de productos que desea agregar: "))
for i in range(cantidad):
    print(f"\n Producto #{i+1}")
    codigo = int(input("Ingrese el codigo del producto: "))
    nombre= input("Ingrese el nombre del producto: ")
    categoria = input("ingrese la categoria del producto: ")
    talla = input("Ingrese la talla: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese stock: "))
    productos[codigo]={
        'nombre' : nombre,
        'categoria' : categoria,
        'talla' : talla,
        'precio' : precio,
        'stock' : stock
    }
print("\nLista de productos")
for codigo, datos in productos.items():
    print(f"Codigo: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Categoria: {datos['categoria']}")
    print(f"Talla: {datos['talla']}")
    print(f"Precio: {datos['precio']}")
    print(f"Stock: {datos['stock']}")
print("\nBuscar producto por codigo")
buscado = int(input("Ingrese el codigo: "))
if buscado in productos:
    print(f"Nombre: {productos[buscado]['nombre']}")
    print(f"Categoria: {productos[buscado]['categoria']}")
    print(f"Talla: {productos[buscado]['talla']}")
    print(f"Precio: {productos[buscado]['precio']}")
    print(f"Stock: {productos[buscado]['stock']}")
