#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
# (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
# la nota más alta que ha sacado y la menor.

notas=[]
contador=0

for i in range(contador,5):
    i=int(input(f"Introduce la nota numero {i} : "))
    if i <=10 and i>=0:
        notas.append(i)
        contador=contador+1
    else:
        print("La nota debe estar entre 0 y 10")

for i in notas:
    print(i," ",end="")

print(f"La nota media es: ",sum(notas)/len(notas))

print(f"La nota maximo es: ",max(notas), "La nota mas baja es: ",min(notas))