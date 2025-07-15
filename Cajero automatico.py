print("Bienvenido")
contador = 0
while contador <3:
    contraseña = input("Introduzca el PIN: ")
    if contraseña == '2020':
        print("contraseña correcta")
        break
    else:
         contador +=1
         print("--contraseña incorrecta--")
         if contador == 3:
             print("Has superado el maximo de intentos")
