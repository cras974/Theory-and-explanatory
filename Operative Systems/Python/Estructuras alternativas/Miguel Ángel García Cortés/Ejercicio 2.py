# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Algoritmo que pida un número y diga si es positivo, negativo o 0.

a=int(input("Dime un numero: "))

if a>=1:
    print("Tu numero es positivo")
elif a == 0:
    print("Tu numero es 0")
elif a<=-1:
    print("Tu numero es negativo")
else:
    print("Introduce un numero valido, no una cadena")