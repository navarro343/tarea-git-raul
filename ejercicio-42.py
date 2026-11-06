cadena = str(input("Di la primera cadena: "))
subcadena = str(input("Di la subcadena: "))

if cadena[:len(subcadena)]== subcadena:
    print("La subcadena empieza por la cadena")
else:
    print("La subcadena no empieza por la cadena")