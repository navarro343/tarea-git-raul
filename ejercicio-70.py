caracter = str(input("Dime una frase o una cadena de carateres: "))

lista = {}

for A in caracter:
    if A in lista:
        lista[A] += 1
    else:
        lista [A] = 1
print (f'{lista}')