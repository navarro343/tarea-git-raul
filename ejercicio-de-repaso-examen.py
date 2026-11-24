#Enunciado
#Una tienda quiere un programa para gestionar sus productos y precios.

#1. Listas
#Pide por teclado los precios de 5 productos y guárdalos en una lista. Después muestra todos los precios, el precio medio, el más alto y el más bajo.

#2. Diccionario
#Crea un diccionario con al menos 4 productos, donde la 
# clave sea el nombre del producto y el valor su stock.
# Pide un nombre por teclado:

#Si existe, muestra su stock y pregunta si quiere modificarlo.
#Si no existe, avisa de que no está en la tienda.

#3. Definición de funciones
#Crea una función Descuento(precio, porcentaje) que
# devuelva el precio una vez aplicado el descuento.
# Pide un precio y un porcentaje, llama a la función
# y muestra el resultado.

#4. Condiciones
#Con el precio final del apartado anterior, muestra:

#"Barato" si es menor de 10
#"Normal" si está entre 10 y 50 (ambos incluidos)
#"Caro" si es mayor de 50

#Además, valida que el precio no sea negativo y
#que el porcentaje esté entre 0 y 100, volviendo
#a pedirlos si no lo están.

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
productos_precios = {"tomate" : 20, "pan" : 5, "jamon" : 3, "cesped":1,"vasijas":8}

peticion = input("Dime uno de los productos: ")

if peticion in productos_precios:
    print(f'El {peticion} si existe en los productos y el valor es {productos_precios[peticion]}')
    cambiar = input("Quieres modificarla (si/no): ")
    if cambiar == "si":
        productos_precios[peticion] = int(input("introduce su nuevo precio: "))
        print(f'El precio {peticion} cambio a {productos_precios[peticion]}')
else:
    print("Este preducto no existe")

#3.......
def descuento(precio, porcentaje):
    precio - porcentaje
    return precio
precio = int(input("Dime el precio: "))
porcentaje = int(input("Di cuanto es el descuento: "))
total = descuento( precio , porcentaje )

print(f'El precio es {precio} su descuento es {porcentaje} y el final del precio es {total}')

#4..........
while precio < 0:
    precio = int(input("El precio es negativo no es valido, vuelve a decir el precio: "))

while porcentaje <0 or porcentaje >100:
    porcentaje = int(input("El porcentaje tienes que estar entre (0 y100), vuelve a decirme cual es:"))

if total<10:
    print("Barato")
elif total <= 50:
    print("Normal")
else:
    print("Caro")