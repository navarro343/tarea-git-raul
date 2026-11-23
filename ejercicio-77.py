def Login(nombre_usuario, contraseña, intentos):
    if nombre_usuario == 'usuario1' and contraseña == 'asdasd':
        return True, intentos
    else:
        return False, intentos + 1

intentos = 0

while intentos < 3:
    nombre_usuario = str(input("Usuario para entrar: "))
    contraseña = str(input("Contraseña: "))
    bien , intentos = Login(nombre_usuario,contraseña, intentos)
    if bien:
        print("Todo correcto, bienvenido")
        break
    else:
        print(f"No es correcto. Te quedan {3 - intentos} intentos")

if intentos == 3:
    print("No puedes seguir te has quedado sin intentos")