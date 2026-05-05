#Realizar un algoritmo que se llame agenda.txt, pedira contactos x del usuario
#De cada contacto lo guardará el nombre y telefono
#Se guardará así: nombre,telefono

#Va a leer la agenda y va a mostrar todos los datos asi :
#Nombre: _____ , Telefono: _____

nuevos=int(input("Cuantos quieres añadir?: "))

f = open("agenda.txt","w")
for i in range (nuevos):
    i=i+1
    nombre=input("Dime el nombre a añadir: ")
    numero=input("Dime el numero a añadir: ")
    f.write(f"{nombre},{numero}\n")
    
f.close()

f = open("agenda.txt","r")

for p in f:
    print(f"Nombre: {nombre}, Telefono: {numero}")
f.close()