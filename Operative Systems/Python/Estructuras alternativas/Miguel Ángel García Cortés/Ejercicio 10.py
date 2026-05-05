# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:
#exteriores
#tangentes exteriores
#secantes
#tangentes interiores
#interiores
#concéntricas

import math

x1=int(input("Dime el valor de x1: "))
x2=int(input("Dime el valor de x2: "))
y1=int(input("Dime el valor de y1: "))
y2=int(input("Dime el valor de y2: "))
r1=int(input("Dime el valor de r1: "))
r2=int(input("Dime el valor de r2: "))


distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

if distancia> r1+r2:
    print("Son exteriores")
elif distancia == r1+r2:
    print("Son tangentes exteriores")
elif r1-r2 < distancia < r1+r2:
    print("Son secantes")
elif distancia == r1-r2:
    print("Son tangentes interiores")
elif 0 < distancia < r1 - r2:
    print("Son interiores")
elif distancia == 0:
    print("Son concentricas")
else:
    print("Error")
print("Programa finalizado")