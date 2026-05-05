# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena=input("Introduce una cadena de caracteres: ")

if any(c.isupper() for c in cadena):
    print("La cadena es de letra mayuscula")
else:
    print("La cadena es minuscula")