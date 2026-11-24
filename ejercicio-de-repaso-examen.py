#Enunciado
#Una tienda quiere un programa para gestionar sus productos y precios.

#1. Listas
#Pide por teclado los precios de 5 productos y guárdalos en una lista. Después muestra todos los precios, el precio medio, el más alto y el más bajo.

#2. Diccionario
#Crea un diccionario con al menos 4 productos, donde la clave sea el nombre del producto y el valor su stock. Pide un nombre por teclado:

#Si existe, muestra su stock y pregunta si quiere modificarlo.
#Si no existe, avisa de que no está en la tienda.

#3. Definición de funciones
#Crea una función Descuento(precio, porcentaje) que devuelva el precio una vez aplicado el descuento. Pide un precio y un porcentaje, llama a la función y muestra el resultado.

#4. Condiciones
#Con el precio final del apartado anterior, muestra:

#"Barato" si es menor de 10
#"Normal" si está entre 10 y 50 (ambos incluidos)
#"Caro" si es mayor de 50

#Además, valida que el precio no sea negativo y que el porcentaje esté entre 0 y 100, volviendo a pedirlos si no lo están.

#1......
productos = []

for A in range(5):
    precios = int(input("Dime el precio de los productos: "))
    productos.append(precios)
print(f'Los precios son {productos}')
print(f'La media es {sum(productos)/5}')
print(f'La mas alta es: {max(productos)}')
print(f'El precio minimo es {min(productos)}')

#2.....
