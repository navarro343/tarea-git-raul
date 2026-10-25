#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#Ejemplo, si se introduce 23 que muestre 32.
numero = int(input("Di el numero de dos cifras elegido: "))

decena = numero // 10
unidad = numero % 10

print(f'El numero invertido es: {(unidad*10)+decena}')