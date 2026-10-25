#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por
#cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0.
#Imprime el resultado obtenido por el estudiante.
correctas = int(input("Cuantas respuestas correctas: "))
incorrectas = int(input("Cuantas respuestas incorrectas: "))
blanco = int(input("Cuantas respuestas en blanco: "))

correctas_f = correctas*5
incorrectas_f = incorrectas*-1
puntos_f = correctas_f+incorrectas_f

print(f'las correctas son{correctas_f} las incorrectas {incorrectas_f} la puntuacion final es: {puntos_f}')