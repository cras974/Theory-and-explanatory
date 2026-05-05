#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) 
# y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
# Debes usar listas. 
# Para simplificarlo vamos a suponer que febrero tiene 28 días.

mes=["enero","febrero","marzo"]
dia=["31","28","31"]

for m,d in zip(mes,dia):
    num=int(input("Dime el numero del mes: "))
    num=num-1
    print(mes[num])
    print(dia[num])