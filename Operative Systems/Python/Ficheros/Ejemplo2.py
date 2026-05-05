#Escribe un programa donde pida 5 numeros, los guarde en un fichero llamado
#numeros.txt, despues lea el contenido y lo muestre por pantalla
#y por ultimo muestre la suma y la media

f = open("numeros.txt","w")
for i in range (5):
    i=i+1
    numero=input("Dime el numero a añadir: ")
    f.write(f"{numero}\n")
    
f.close()

f = open("numeros.txt","r")

suma = 0
contador = 0

for linea in f:
    n = int(linea)
    suma = suma + n
    contador = contador+1

f.close()

media = suma / contador

print(f"La suma vale: {suma}")
print(f"La media vale: {media}")