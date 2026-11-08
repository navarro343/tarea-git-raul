meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
         "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input("Introduce el numero de mes (1-12): "))

while mes < 1 or mes > 12:
    print("El mes tiene que estar entre 1 y 12")
    mes = int(input("Introduce el numero de mes (1-12): "))

print(f"El mes {mes} es {meses[mes - 1]} y tiene {dias[mes - 1]} dias")
