# Vamos a pedir 5 nombres, los va a guardar en un fichero llamado nombres.txt

import os

os.system("cls")

f = open("nombres.txt","a")
for i in range (5):
    i=i+1
    nombre=input("Dime el nombre a añadir: ")
    f.write(f"Nombre numero {i} {nombre} \n")
    
f.close()

f = open("nombres.txt","r")
contenido = f.read()
print(contenido)
f.close()