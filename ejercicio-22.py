import random

numero_secreto = random.randint(1, 100)
intentos_totales = 10
intentos_restantes = intentos_totales

print(f"Adivina el número secreto, tienes {intentos_totales} intentos")

while intentos_restantes > 0:
    numero = int(input("Introduce un número: "))

    if numero == numero_secreto:
        intentos_usados = intentos_totales - intentos_restantes + 1
        print(f"Muy bien, lo has acertado. El número es: {numero_secreto}.")
        print(f"Lo has conseguido en {intentos_usados} intentos.")
        break
    elif numero < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

    intentos_restantes -= 1
    print(f"Te quedan {intentos_restantes} intentos")

else:
    print("Oh, qué mala suerte, no lo has acertado. No te quedan intentos.")
    print(f"El número secreto que había generado era el: {numero_secreto}")