#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el
#plano. Calcula y muestra la distancia entre ellos.
numero1_x1 = float(input("El numero para x1 es: "))
numero2_y1 = float(input("El numero para y1 es: "))
numero1_x2 = float(input("El numero para x2 es: "))
numero2_y2 = float(input("El numero para y2 es: "))

print(f'La distancia entre ambos puntos es de {(((numero1_x2-numero1_x1)**2)+((numero2_y2-numero2_y1)**2))**0.5}')