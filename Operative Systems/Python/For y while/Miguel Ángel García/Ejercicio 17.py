# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
# Para esto, se registran los días que trabajó y las horas de cada día. 
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

horas=0
total=0
cobra=0
conthora=0
respuesta=1
empleado=0

while True:
    
    respuesta=input("Pon espacio para salir, cualquier otra cosa para calcular un trabajador: ")
    if respuesta == " ":
        break
    else:
        cobra=int(input("A cuanto cobra la hora?: "))
        
        for dia in range(1, 7):
            horas=int(input("Dime cuantas hora a trabajado el dia " + str(dia) +" : "))
            total=total+horas*cobra
            conthora=horas+conthora

        empleado=empleado+1
        print ("Las horas totales han sido ",conthora)
        print ("El cobro total de esta semana ha sido ",total)

print("El pago ha sido", total, "sobre", empleado, "empleados")