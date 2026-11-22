def EsMultiplo(a ,b):
    if a % b == 0:
        return True
    else:
        return False

numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: "))

if EsMultiplo(numero1, numero2):
    print(f'{numero1} es multiplo de {numero2}')
elif EsMultiplo(numero2,numero1):
    print(f'{numero2} es multiplo de {numero1}')
else:
    print(f'ninguno es un multiplo')

EsMultiplo(numero1 , numero2)