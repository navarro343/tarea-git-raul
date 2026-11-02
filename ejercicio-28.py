superior = int(input("Dime el intervalor mayor: "))
inferior = int(input("Dime el intervalor menor: "))

while superior < inferior:
    print("El limite superior tiene que ser mayor")
    superior = int(input("Dime el intervalor mayor: "))
    inferior = int(input("Dime el intervalor menor: "))

suma = 0
intervalo = 0
fuera = 0

numero = int(input("Dime un numero que quieras intentar solucionar: "))

while numero != 0:
    if numero < superior and numero > inferior:
         suma += numero
    elif numero == superior or numero == inferior:
        intervalo += 1
    else :
        fuera += 1
    numero = int(input("Dime un numero que quieras intentar solucionar: "))

print(f"La suma de los numeros dentro del intervalo es: {suma}")
print(f"Numeros fuera del intervalo: {fuera}")
if intervalo == superior or intervalo == inferior:
    print(f"Has puesto numeros que son igual a los intervalos {intervalo}")
else:
    print("No has introducido ningun numero igual a los limites")