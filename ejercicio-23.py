numero = int(input("Introduce numeros(con el 0 se termina): "))

suma = 0
cantidad = 0

while numero != 0:
    suma += numero
    cantidad += 1
    numero = int(input("Introduce numeros(con el 0 se termina): "))
if cantidad > 0:
    media = suma / cantidad
    print(f'La suma es {suma} la media es {media}')
else: 
    print("El numero introducido no es valido (no puede ser 0)") 