n=int(input("Introduce un numero del 1 al 10:"))

while True:
    if n <1 or n >10:
        print("Error, esta fuera de los limites.")
        n=int(input("Introduce un numero del 1 al 10:"))
    else:
        break
    
nombre_fichero = "tabla-" + str(n) + ".txt"

#Creando fichero

f = open(nombre_fichero, "w")
for i in range(1,11):
    f.write(str(n) + "x" + str(i) + "=" + str(n*i) + "\n")
f.close()

#Lectura

f = open(nombre_fichero,"r")
print(f.read())
f.close()