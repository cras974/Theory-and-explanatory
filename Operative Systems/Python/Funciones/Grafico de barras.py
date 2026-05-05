import matplotlib.pyplot as plt

#Datos
categorias = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]

ventas = [12, 19, 8, 15, 22]

#Crear el grafico de barras

plt.bar(categorias, ventas, color=['green','red','yellow','pink','purple'])

#Etiquetas y título
plt.xlabel("Meses")
plt.ylabel("Ventas en miles")
plt.title("Ventas Mensuales")
plt.legend()

#Mostrar el grafico
plt.show()