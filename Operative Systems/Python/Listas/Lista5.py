# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), 
# y posterior ordene los elementos de menor a mayor.

import random

lista=[]

for i in range(0,10):
    lista.append(random.randint(1,100))

lista=sorted(lista)

for i in lista:
    print(i," ",end="")