notas = []

for A in range(5): 
    nota = float(input("Introduce las 5 notas: "))
    while nota < 0 or nota > 10:
        print(f'Las notas introducidas no son validas tiene que ser entre 0 y 10')
        nota = float(input("Introduce las 5 notas: "))
    notas.append(nota)

media = sum(notas) / 5

print(f'La nota media es {media}')
print(f'Las notas son {notas}')
print(f'La nota maxima es {max(notas)}')
print(f'La nota minima es {min(notas)}')