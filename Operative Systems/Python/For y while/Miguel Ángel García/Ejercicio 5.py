# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.


respuesta=0

while respuesta != " ":
    print("Escribe un espacio para salir")
    respuesta=input("Dme un caracter: ").lower()
    if respuesta == "a" or respuesta == "e" or respuesta == "i" or respuesta == "o" or respuesta == "u":
        print("La letra es una vocal")
    elif respuesta == " ":
        break
    else:
        print("La letra no es vocal")
    