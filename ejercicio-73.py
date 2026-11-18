agenda = {}

choice = None

while choice != '5':
    choice = input('''
¡Bienvenido a nuestra agenda! elige una:
1- Añadir
2- Buscar
3- Listar
4- Borrar
5- Salir
    ''')
    if choice =="1":
        nombre = str(input("Cual es el nombre: "))
        if nombre in agenda:
            print(f'El nombre es {nombre} y el telefono {agenda[nombre]}')
            cambiar = str(input("Quieres modificarlo (si/no): "))
            if cambiar == "si":
                agenda[nombre] = input("Mete el nuevo telefono: ")
        else:
            agenda[nombre] = input("El contato no existe, el telefono es:")

    elif choice =="2":
        cadena = input("Que contactos buscas: ")
        for nombre in agenda:
            if nombre.startswith(cadena):
                print(f'{agenda[nombre]}: {agenda} ')
        else:
            print(f'El contacto no existe, agregalo pulsando otra vez 1')

    elif choice == "3":
        for nombre in agenda:
            print(f'{nombre}: {agenda[nombre]}')

    elif choice == "4":
            nombre = str(input("Cual es el nombre a borrar: "))
            if nombre in agenda:
                borrar = input(f'Seguro que quiere borrar {nombre} (si/no): ')
                if borrar == "si":
                    del agenda[nombre]
            else: 
                print(f'El nombre no existe')
    
    elif choice != "5" and "0":
        print("Esta opcion no es valida")