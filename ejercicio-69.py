numero = int(input("Dime un numero para el diccionario:"))

cuadrados = {}

for A in range(1,numero+1):
    cuadrados[A] =A**2
print(f'El diccionario seria {cuadrados}')