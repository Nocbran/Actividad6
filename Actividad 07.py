estudiantes = {}
propcurso = {}

def regestudiantes():
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
                'tarea' : notarea,
                'parcial' : notaparcial,
                'proyecto' : notaproyecto
        }
    estudiantes[carnet] = {
        'nombre' : nomcompleto,
        'edad' : edad,
        'carrera' : carrera,
        'cursos' : contcurso
    }

def mostrarestudiante():
    for carnet, datos in estudiantes.items():
        print(f"\nCarnet: {carnet}")
        print(f"\nNombre: {datos['nomcompleto']}")
        print(f"\nEdad: {datos['edad']}")
        print(f"\nCarrera: {datos['carrera']}")
        if datos['propcuros']:
            print("Cursos inscritos")
            for propcurso, notas in datos['propcuros'].items():
                promedio = (notas['tarea']+notas['parcial']+notas['proyecto'])
                print(f'{propcurso}')
                print(f"Tarea: {notas['tarea']}")
                print(f"Parcial: {notas['parcial']}")
                print(f"Proyecto: {notas['Proyecto']}")
                print(f"Promedio: {promedio:.f}")

def buscaestudiante():
    carnet = input("Ingrese el carnet del estudiante")
    if carnet in estudiantes:
        datos = estudiantes[carnet]
        print(f"\nCarnet: {carnet}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Edad: {datos['edad']}")
        print(f"Carrera: {datos['carrera']}")
        if datos['propcursos']:
            print("Cursos inscritos")
            for propcurso, notas in datos['propcuros'].items():
                promedio = (notas['tarea']+notas['parcial']+notas['proyecto'])
                print(f'{propcurso}')
                print(f"Tarea: {notas['tarea']}")
                print(f"Parcial: {notas['parcial']}")
                print(f"Proyecto: {notas['Proyecto']}")
                print(f"Promedio: {promedio:.f}")



while True:
    print("\n********MENU PRINCIPAL*******")
    print("1. Registrar estudiantes ")
    print("2. Mostrar todos los estudiantes y sus cursos ")
    print("3. Buscar estudiante por carnet ")
    print("4. Salir ")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == "1":
        regestudiantes()
    elif opcion == '2':
       mostrarestudiante()
    elif opcion == '3':
        buscaestudiante()
    elif opcion == '4':
        print("Asta pronto")
        break
