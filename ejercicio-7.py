#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
#horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minutos_completos = float(input("Dime la cantidad de minutos que deseas modifciar o ver: "))

print(f'Las horas serian: {minutos_completos//60}y los minutos: {minutos_completos%60}')