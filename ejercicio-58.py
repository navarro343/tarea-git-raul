nombres = []
edades = []

nombre = input("Dime el alumno (* para terminar): ")

while nombre != "*":
    edad = int(input("Dim la edad: "))
    nombres.append(nombre)
    edades.append(edad)
    nombre = input("Dime el alumno (* para terminar): ")

print("Alumnos mayores de edad:")
for i in range(len(nombres)):
    if edades[i] >= 18:
        print(f"{nombres[i]} ({edades[i]} años)")

if len(edades) > 0:
    mayor = max(edades)
    print("Alumnos que tiene mas edad:")
    for i in range(len(nombres)):
        if edades[i] == mayor:
            print(f"{nombres[i]} ({edades[i]} años)")
else:
    print("dime algun alumno")