#Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
#Entonces se debe imprimir el vector (sólo los elementos introducidos).

lista=[]

while True:
    print("Si quieres salir introduce un valor negativo")
    mas=int(input("Introduce el valor a introducir: "))
    if mas >=0:
        lista.append(mas)
    elif mas <0:
        print("Saliendo del bucle")
        break

for i in lista:
    print(i," ",end="")