estudiantes = {}
propcurso = {}

cantidad = int(input(f"\n¿Cuántos estudiantes desea ingresar?: "))
for i in range(cantidad):
    print(f"\nEstudiante #{i+1}")
    carnet = int(input("Ingrese el numero de carnet: "))
    nomcompleto = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    carrera = input("Ingrese la carrera: ")
    contcurso= int(input("Cuantos cursos se asignara?: "))
    for j in range(contcurso):
        print(f"\nCurso #{j+1}")
        nomcurso = input("Nombre del curso: ")
        notarea = int(input("Nota de la tarea 0-100: "))
        notaparcial = int(input("Nota de parcial 0-100: "))
        notaproyecto = int(input("Nota de proyecto 0-100: "))
        propcurso[nomcurso] = {
            'tarea' : nomcurso,
            'parcial' : notarea,
            'proyecto' : notaparcial
        }
    estudiantes[carnet] = {
        'nombre' : nomcompleto,
        'edad' : edad,
        'carrera' : carrera,
        'cursos' : contcurso
    }


"""__________________________________________________________
print("********MENU PRINCIPAL*******")
print("1. Registrar estudiantes ")
print("2. Mostrar todos los estudiantes y sus cursos ")
print("3. Buscar estudiante por carnet ")
print("4. Salir ")
"""