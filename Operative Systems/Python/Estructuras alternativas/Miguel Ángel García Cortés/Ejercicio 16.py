# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, 
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, 
# y a partir del décimo minuto, 50 céntimos.
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. 
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

dia=input("Que momento es (Domingo, Mañana, Tarde): ")

duracion=int(input("Cuanto tiempo en minutos ha durado la llamada: "))
total = 0


if duracion <= 5:
    total=5*1
elif duracion >= 5 and duracion <=8:
    total=5*1 + (duracion-5) * 0.8
elif duracion >= 8 and duracion<=10:
    total=5*1 + 3*0.8 + (duracion-8)*0.7
elif duracion >= 10:
        total=5*1 + 3*0.8 + 2*0.7 + (duracion-10)*0.5
else:
    print("Introduzca un numero")
    
conjunto=0

if dia == "Domingo":
    conjunto=(total*3)/100
elif dia == "Mañana":
    conjunto=(total*15)/100
elif dia == "Tarde":
    conjunto=(total*10)/100
else:
    print("Introduzca un momento del dia correcto")

print("El costo total es", conjunto,"€")