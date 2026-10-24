#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#● 55% del promedio de sus tres calificaciones parciales.
#● 30% de la calificación del examen final.
#● 15% de la calificación de un trabajo final.
nota_1 = float(input("La primera nota es: "))
nota_2 = float(input("La segunda nota es: "))
nota_3 = float(input("La tercer nota es: "))
examen_final = float(input("La nota del examen final es: "))
trabajo = float(input("La nota del trabajo es: "))

media_notas = (nota_1+nota_2+nota_3)/3

print(f'La nota del curso es: {(media_notas*0.55)+(examen_final*0.30)+(trabajo*0.15)}')