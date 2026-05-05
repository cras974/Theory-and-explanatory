# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

a=int(input("Dime un numero: "))
b=int(input("Dime otro numero: "))

if b == 0:
    print("El segundo numero no puede ser 0")
else:
    print(a/b)