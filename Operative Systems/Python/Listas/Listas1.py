#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente 
#muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

lista=[]
numero=0

for i in range(0,11):
    lista.append(random.randint(1,10))

for i in lista:
    print(i," ",end="")
    
print ("Simple")

listacuadraro=[]
listacuadraro=lista

for i in listacuadraro:
    print(i**2," ",end="")

print ("Cuadrado")

listacubo=[]
listacubo=lista

for i in listacubo:
    print(i**3," ",end="")

print ("Cubo")