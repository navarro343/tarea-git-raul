introduce = str(input("Di la primera cadena: "))
subcadena = str(input("Di la subcadena: "))

if introduce[:len(subcadena)]== subcadena:
    print("La cadena empieza por la subcadena")
else:
    print("La cadena no empieza por la subcadena")