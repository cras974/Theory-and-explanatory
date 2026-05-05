#Autor: Miguel Ángel García Cortés
#Version 1.0
#Ejercicio 2
#A)                   

numeros=[]
num=0

while True:
    num=int(input(" Introduce un numero menor que 0 para continuar | Dime un numero entero: "))
    if num >= 0:
        numeros.append(num)
    else:
        print ("Saliendo")
        break

for i in numeros:
    print(i," ",end="")

print ("| Numeros |")
    
pares=[]
impares=[]

for i in numeros:
    if (i % 2) == 0:
        pares.append(i)

for i in numeros:
    if (i % 2) != 0:
        impares.append(i)

for i in pares:
    print(i," ",end="")
    
print ("| Pares |")
    
for i in impares:
    print(i," ",end="")

print ("| Impares |")
