# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

tiempo=int(input("Dime una cantidad de minutos: "))

minutos=tiempo%60
horas=int(tiempo/60)

print("En horas y minutos son", horas,"horas", minutos,"minutos")