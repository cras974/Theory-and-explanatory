import matplotlib.pyplot as plt

#Datos
x = [1,2,3,4,5]

y = [10,15,7,20,5]


#Crear el grafico

plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Ventas")

#Etiquetas y título
plt.xlabel("Días")
plt.ylabel("Ventas")
plt.title("Ventas Diarias")
plt.legend()

#Mostrar el grafico
plt.show()