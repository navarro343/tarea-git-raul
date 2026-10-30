caracter = str(input("introduce caracteres(al poner espacio se termina): "))
while caracter != " ":
    if caracter in caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" :
        print("vocal")
    else:
        print("no vocal")
    caracter = input("introduce un caracter caracter(espacio para terminar): ")