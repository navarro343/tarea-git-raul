#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre = str(input("Di tu nombre: "))
apellido1 = str(input("Di tu apellido1: "))
apellido2 = str(input("Di tu apellido2: "))

print(f'Tus iniciales son {nombre[0].upper()}.{apellido1[0].upper()}.{apellido2[0].upper()}.')