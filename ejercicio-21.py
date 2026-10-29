numero = int(input("Dime el numero: "))
factorial = 1

for A in range (1, numero + 1):
    factorial = factorial * A
print(f'El factorial de {numero}! es: {factorial}')    
