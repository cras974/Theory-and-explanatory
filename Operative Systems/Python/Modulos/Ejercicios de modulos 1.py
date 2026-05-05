#Escribir un programa que pregunte al usuario por las ventas de un rango de años 
#y muestre por pantalla un diagrama de líneas con la evolución de las ventas

import matplotlib.pyplot as plt

anyo = []
ventas = []

print("Recuerda que y e X deben tener la misma cantidad de valores")
while True:
    valoranyo = int(input("0 Para salir | Dime un valor de años por año: "))
    if valoranyo == 0:
        print("Años introducidos")
        print("------------------")
        break
    else:
        anyo.append(valoranyo)

while True:
    valorventas = int(input("0 Para salir |Dime un valor de ventas: "))
    if valorventas == 0:
        print("Ventas introducidas")
        print("------------------")
        break
    else:
        ventas.append(valorventas)


plt.plot(anyo, ventas, marker='o', linestyle='-', color='b', label="Ventas")

plt.xlabel("Años")
plt.ylabel("Ventas")
plt.title("Ventas por año")

#Mostrar el grafico
plt.show()