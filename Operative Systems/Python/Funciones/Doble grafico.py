import matplotlib.pyplot as plt

#Datos
x = [1,2,3,4,5,6,7]

y1 = [5,7,10,10,12,9,10]

y2 = [10, 9, 2, 6, 8, 1, 9]

#Crear una figura con 2 graficos

plt.figure(figsize=(10,4))

#Primer grafico
plt.subplot(1,2,1)
plt.plot(x, y1, marker='o', color='blue')
plt.title("Grafico 1")

#Segundo grafico
plt.subplot(1,2,2)
plt.bar(x,y2, color='red')
plt.title("Grafico 2")

#Mostrar el grafico
plt.show()