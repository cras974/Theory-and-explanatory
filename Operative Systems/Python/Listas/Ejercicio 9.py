#Autor: Paco Fernandez
#Version: 1.0
#Queremos guardar la temperatura mínima y máxima de 5 días.
#Realiza un programa que de la siguiente información:
#La temperatura media de cada día
#Los días con menos temperatura
#Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
#si no existe ningún día se muestra un mensaje de información.
minima = []
maxima = []

for i in range(5):
    tmin = float(input("Introduce la temperatura mínima del día: "))
    tmax = float(input("Introduce la temperatura máxima del día: "))
    minima.append(tmin)
    maxima.append(tmax)


print("La temperatura media de cada dia")
for i in range(5):
    media = (minima[i] + maxima[i]) / 2
    print("La temperatura media del dia", i+1,media)

#Dias con temperatura minima
for p in range(5):
   if minima[p] == min(minima):
       print("Dia", p+1, min(minima),"ºC")

#Dias que coinciden con temperatura maxima
temperatura = float(input("Introduce una temperatura: "))
contador_max = 0
for j in range(5):
    if maxima[j] == temperatura:
       print("Dia", j+1, temperatura,"ºC")
       contador_max += 1


if contador_max == 0:
    print("No existe ningun dia que coincida con esa temperatura")