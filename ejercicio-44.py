palabras = str(input("Dime una frase: "))
espacios = 0

for A in palabras:
    if A ==" ":
        espacios +=1

print(f'La frase tiene {espacios + 1} palabras')