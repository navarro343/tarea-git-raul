def EscribirCentrado(texto):
    espacios = 40 - len(texto) // 2
    print(f'{" " * espacios}{texto}')
    print(f'{" " * espacios}{"=" * len(texto)}')

mensaje = input("Dime el texto a introducir: ")
EscribirCentrado(mensaje)