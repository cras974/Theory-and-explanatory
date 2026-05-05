import matplotlib.pyplot as plt
import os

os.system("cls")

producto = []

cantidad = []

while True:
    
    print("1) Añadir datos")
    print("| Escribe fin para salir")
    print("")
    opcion = input("Dime la opcion: ")
    
    if opcion == "1":
        
        producto.append(input("Dime el producto vendido: "))
        cantidad.append(int(input("Dime la cantidad del producto vendido: ")))
    
    elif opcion == "fin":
        
        break
    
    else:
        
        print("Escribe una opcion correcta")

color=input("Dime el color del grafico en ingles o hexadecimal: ")

plt.bar(producto,cantidad,color=color)
plt.title("Productos vendidos")
plt.xlabel("Productos")
plt.ylabel("Ventas")
plt.legend("Esto es un grafico productos-ventas de la tienda")
plt.show()