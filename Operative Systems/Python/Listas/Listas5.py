#Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. 
#Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista=[]
contador=0

for i in range(0,5):
    i=input("Introduce una cadena de caracteres: ")
    contador=contador+1
    print("Este es el input", contador)
    lista.append(i)

listacopia=[]
listacopia=sorted(lista,reverse=True)

for i in listacopia:
    print(i," ",end="")