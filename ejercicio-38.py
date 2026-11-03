import time

horas = 0
minutos = 0
segundos = 0
segundos_iniciales = 0

while True:
    time.sleep(1)
    segundos_iniciales += 1
    horas = segundos_iniciales // 3600
    minutos = segundos_iniciales %3600 // 60
    segundos = segundos_iniciales % 60
    print(f'Timer:{horas}:{minutos}:{segundos}')