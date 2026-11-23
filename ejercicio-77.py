def Login(nombre_usuario, contraseña):
    if nombre_usuario == 'usuario1' and contraseña == 'asdasd':
        return True
    else:
        return False
    
intentos = 0

while intentos < 3:
    nombre_usuario = str(input("Usuario para entrar: "))
    contraseña = str(input("Contraseña: "))
    bien , intentos = Login(nombre_usuario,contraseña, intentos)
    if bien:
        print("Todo correcto, bienvenido")
        break
    else:
        intentos += 1
        print(f"No es correcto. Te quedan {3 - intentos} intentos")

if intentos == 3:
    print("No puedes seguir te has quedado sin intentos")