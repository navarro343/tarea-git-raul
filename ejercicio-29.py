#Escribe un programa que dados dos números, uno real (base) y un entero positivo
#(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
#de potencia.

base = int(input("Di la base: "))
exponente = int(input("Di el exponente: "))

resultado = 1

for A in range(exponente):
    resultado = resultado * base

print(f"{base} elevado a {exponente} es: {resultado}")