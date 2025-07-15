estudiantes ={}
cantidad = int(input(f"\nIngrese cantidad de estudiantes"))
for i in range(cantidad):
    print(f"\n estudiante #{i+1}")
    carne = input("Ingrese carnet: ")
    nombre= input("Ingrese: ")
    edad = int(input("ingrese edad: "))
    carrera = input("Ingrese carrera: ")
    estudiantes[carne]={
        "nombre" : nombre,
        "edad" : edad,
        "carrera" : carrera
    }
print("\nLista de estudiantes")
for carne, datos in estudiantes.items():
       print(f"Carne : {carne}")
       print(f"Nombre: {datos[nombre]}")
       print(f"Edad: {datos[edad]}")
       print(f"Carrera: {datos[carrera]}")
print("Buscar estudiante")
buscado = input("Ingrese el numero de carne: ")
if buscado in estudiantes:
    print(f"Nombre: {estudiantes[buscado]["nombre"]}")
    print(f"Edad: {estudiantes[buscado]["edad"]}")
    print(f"Carrera: {estudiantes[buscado]["carrera"]}")
