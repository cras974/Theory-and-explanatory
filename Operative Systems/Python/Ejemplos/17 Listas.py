#Crear un programa que añada números a una lista hasta que introducimos un número negativo. 
#A continuación debe crear una nueva lista igual que la anterior pero eliminando los números duplicados. 
#Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

lista=[]
numero=int(input("Introduce un numero (Si es negativo saldrá del menú): "))

while numero >= 0:
    lista.append(numero)
    numero=int(input("Introduce un numero (Si es negativo saldrá del menú): "))


listacopia=[]

for num in lista:
    if num not in listacopia:
        listacopia.append(num)
    else:
        print("El numero ",num," ya está en la lista o es negativo")
        
for num in listacopia:
    print(num," Esta en listacopia")
    