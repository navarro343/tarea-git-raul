#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de
#viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la
#hora de llegada a la ciudad B.

horas = int(input("Cual es la hora a la que salio: "))
minutos = int(input("Cuales son los minutos a la que salio: "))
segundo = int(input("Cual es los segundos a la que salio: "))

viaje = int(input("Tiempo que tarda en llegar en segundos: "))

horas = horas*3600
minutos = minutos*60

tiempo_actual = (horas+minutos+segundo)

trajecto = (tiempo_actual+viaje)

hora_llegada = trajecto // 3600
resto_segundos = trajecto % 3600
minuto_llegada = resto_segundos // 60
segundo_llegada = resto_segundos % 60

print(f'Llegara a las {hora_llegada} h {minuto_llegada} m {segundo_llegada} S')