#Autor: Miguel Ángel García
#Version: 1.0
#Primeros pasos de listas

import os

os.system("cls")

lista=[]
lista1=[1,2,3,4,5]
lista2=["a","b","c","d","e"]
notas=[2.5,10,9.3,8.2,4.4,6.5]

#Recorrer listas

'''

for num,letra in zip(lista1,lista2):
    print(num,letra)
    
'''

#Operaciones con listas

lista1 = lista1 + [6,7,8]

'''

for num in lista1:
    print (num)
    
'''    

#Funciones tipicas de listas

print("Longitud: ",len(lista1))
print("Suma: ",sum(lista1))
print("Maximo: ",max(lista1))
print("Minimo: ",min(lista1))
print("Notas ordenadas: ",sorted(notas))
print("Notas ordenadas al contrario: ",sorted(notas,reverse=True))
