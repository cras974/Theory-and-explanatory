# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia.
# No se puede utilizar el operador de potencia.

base=int(input("Dime la base: "))
exponente=int(input("Dime el exponente: "))

import math

print("El resultado es : ",math.pow(base, exponente))