#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una
#distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para
#ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con
#esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

vehiculo1 = float(input("Cual es la velocidad del primer vehiculo: "))
vehiculo2 = float(input("Cual es la velocidad del segundo vehiculo: "))
D = float(input("Cual es la distancia entre ambos coches: "))

if vehiculo1 <= vehiculo2: print("El primer vehiculo tiene que ser mas rapido para poder alcanzar al segundo")
else: print(f'El primer coche tardara {(D/(vehiculo1/vehiculo2))*60} minutos')