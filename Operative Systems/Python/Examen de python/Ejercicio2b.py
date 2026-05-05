#Autor: Miguel Ángel García Cortés
#Version 1.0
#Ejercicio 2
#B)

nota=int(input("Dime una nota: "))
edad=int(input("Dime la edad: "))
sexo=input("Dime el sexo |F / M|: ")

if nota >= 5 and edad >= 18 and sexo == "F":
    print("ACEPTADA")

elif nota >= 5 and edad >= 18 and sexo == "M":
    print("POSIBLE")
    
else:
    print("NO ACEPTADA")