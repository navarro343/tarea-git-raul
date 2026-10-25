#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un
#algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las
#dos variables.
A = float(input("Dime la primera variable: "))
B = float(input("Dime la segunda variable: "))

intercambio = A
A = B
B = intercambio

print(f'La variable A vale: {A} la B vale: {intercambio} ambas son {A+B}')