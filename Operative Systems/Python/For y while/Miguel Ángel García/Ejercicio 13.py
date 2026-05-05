# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y 
# requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

horas=0
total=0
cobra=int(input("A cuanto cobra la hora?: "))
conthora=0

for dia in range(1, 7):
    horas=int(input("Dime cuantas hora a trabajado el dia " + str(dia) +" : "))
    total=total+horas*cobra
    conthora=horas+conthora

print ("Las horas totales han sido ",conthora)
print ("El cobro total de esta semana ha sido ",total)