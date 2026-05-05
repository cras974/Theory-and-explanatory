#Autor: Miguel Ángel García
#Version: 1.0
#Realizar un programa que inicialice una lista con 10 valores aleatorios, crea una lista con el cuadrado de estes valores
#Y otra con el cubo de estos valores

import random

numeros=[]

cuadrado=[]

cubo=[]

contador=0

while contador <= 10:
    numeros = numeros + [random.randint(1,10)]
    contador= contador+1
    
for num in numeros:
    print (num)