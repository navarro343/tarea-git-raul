#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
#pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).
monedas_2euro = int(input("Cuantas monedas de 2 euros son: "))
monedas_1euro = int(input("Cuantas monedas de 1 euros son: "))
monedas_50cent = int(input("Cuantas monedas de 50 centimos son: "))
monedas_20cent = int(input("Cuantas monedas de 20 centimos son: "))
monedas_10cent = int(input("Cuantas monedas de 10 centimos son: "))

dinero_total= (monedas_2euro *2)+(monedas_1euro*1)+(monedas_50cent*0.50)+(monedas_20cent*0.20)+(monedas_10cent*0.10)

euros_totales = int(dinero_total)

centimos = round((dinero_total-euros_totales)*100)
print(f'El dinero total es: {dinero_total:.2} tus euros son: {euros_totales} y los centimos son: {centimos}')