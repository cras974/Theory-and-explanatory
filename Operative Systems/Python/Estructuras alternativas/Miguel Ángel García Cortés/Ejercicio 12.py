# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

anyo=int(input("Dime un año: "))

p4=anyo%4
p100=anyo%100
p400=anyo%400

if p4 == 0 and p100 != 0:
    
    print("El año es bisiesto")
    
elif p4 == 0 and p400 == 0:
    
    print("El año es bisiesto")

else:
    print ("El año NO es bisiesto")