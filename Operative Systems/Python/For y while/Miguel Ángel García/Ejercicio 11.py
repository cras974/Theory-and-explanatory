# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Escribe un programa que diga si un número introducido por teclado es o no primo. 
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math
numero=int(input("Dime un numero: "))
primo=0
raiz=int(math.sqrt(numero))

for i in range(2, raiz + 1):
        if numero % i == 0:
            primo = "no"
            break

if primo == "no":
    print("EL numero no es primo")
else:
    print("El numero es primo")