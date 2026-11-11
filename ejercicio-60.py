tabla = []

for B in range(5):
    fila = []
    for A in range(5):
        numero = int(input(f"Di el valor de la fila {B + 1}, columna {A + 1}: "))
        fila.append(numero)
    tabla.append(fila)

for B in range(5):
    suma_fila = 0
    for A in range(5):
        suma_fila += tabla[B][A]
    print(f"Suma de la fila {B + 1}: {suma_fila}")

for A in range(5):
    suma_columna = 0
    for B in range(5):
        suma_columna += tabla[B][A]
    print(f"Suma de la columna {A + 1}: {suma_columna}") 