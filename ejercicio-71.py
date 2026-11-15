precios_productos = {"platano" :2.3, "melocoton" :2,"pera" : 1.3, "uva": 1, "naranja": 1.7}

while True:
    frutas = str(input("Dime una fruta(platano, melocoton, pera, uva, naranja): "))
    cantidad = int(input("Dime los kilos que vas a comprar: "))
    if frutas in precios_productos:
        print(f'La fruta esta a {precios_productos[frutas]} el total seria {precios_productos[frutas]*cantidad}')
    else:
        print(f'Esta fruta no esta en la tienda')
    if input("Quieres seguir (si/no): ")== "no":
        break