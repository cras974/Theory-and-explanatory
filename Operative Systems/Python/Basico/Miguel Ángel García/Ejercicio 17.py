# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

hora=int(input("Hora de salida: "))
minuto=int(input("Minuto de salida: "))
segundo=int(input("Segundos de salida: "))


print("La hora de salida es", hora, "horas", minuto, "minutos", segundo, "segundos")

retardo=int(input("Cuantos segundos tardará en llegar a la otra ciudad: "))

horaretardo=int(retardo/3600)
minutoretardo=int(retardo%3600/60)
segundoretardo=int(retardo%60)

print("La hora de llegada es", hora+horaretardo, "horas", minuto+minutoretardo, "minutos", segundo+segundoretardo, "segundos")