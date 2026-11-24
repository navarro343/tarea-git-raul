def pasosegundos(horas, minutos, segundos):
    pasado_segundos = horas*3600+minutos*60+segundos
    return pasado_segundos

def paso_h_m_s(segundos):
    horas = segundos//3600
    resto = segundos%3600
    minutos = resto //60
    segun = resto%60
    return horas, minutos, segun

marcar = ""

while marcar != "3":
    print("para hacer el paso a segundos = 1")
    print("Para hacer el paso de segundos a horas, minutos y segundos = 2")
    print("Para salir o terminar = 3")
    marcar = input("Eligue una opcion de las anterior: ")

    if marcar == "1":
        h = int(input("Dime cuantas horas: "))
        m = int(input("Dime cuantos minutos: "))
        s = int(input("Dime cuantos segundos: "))
        total = pasosegundos(h,m,s)
        print(f'las {h} horas, los {m} minutos y los {s} segundos son en total de segundos es {total}')
    
    elif marcar == "2":
        segun = int(input("Cuentos segundo vamos a modificar: "))
        h ,m ,s = paso_h_m_s(segun)
        print(f"Los segundos totales son {segun} que son {h} horas {m} minutos y {s} segundos")
    
    elif marcar == "3":
        print("Terminado, gracias por usar el prgrama")
    else:
        print("Esa no es valida")
