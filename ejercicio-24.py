cantidad = int(input("Dime cuantos datos vas a introducir: "))
mayores = 0
menores = 0
iguales = 0

for a in range (cantidad):
    numero = int(input("Dime un numero: "))
    if numero > 0: 
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
print(f'Los mayores son: {mayores}')
print(f'Los menores son: {menores}')
print(f'Los iguales son: {iguales}')