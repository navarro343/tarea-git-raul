primer_numero = int(input("Dime el primer número: "))
segundo_numero= int(input("Dime el segundo número: "))
for A in range(primer_numero, segundo_numero+1):
    if A % 2 == 0:
        print(f"Los pares son: {A}")