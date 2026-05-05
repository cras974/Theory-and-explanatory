# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

import os

opcion=0
numero1=0
numero2=0

while True:
    os.system("cls")
    print("_______________________")
    print(" ")
    print("1) Sumar valores")
    print("2) Restar valores")
    print("3) Dividir valores")
    print(" ")
    print("Escribe salir para finalizar")
    print(" ")
    opcion=input("Elige una opcion del menu: ").lower()
    print("_______________________")
    
    if opcion=="1":
        print(" ")
        numero1=int(input("Dime el primer numero: "))
        numero2=int(input("Dime el segundo numero: "))
        print("La suma es: ",numero1+numero2)
        input("Pulsa enter para continuar")
    elif opcion=="2":
        print(" ")
        numero1=int(input("Dime el primer numero: "))
        numero2=int(input("Dime el segundo numero: "))
        print("La resta es: ",numero1-numero2)
        input("Pulsa enter para continuar")
        
    elif opcion=="3":
        print(" ")
        numero1=int(input("Dime el primer numero: "))
        numero2=int(input("Dime el segundo numero, que no sea 0: "))
        if numero2==0:
            print("El numero 2 no puede ser 0")
            input("Pulsa enter para continuar")
        else:
            print("La suma es: ",numero1/numero2)
            input("Pulsa enter para continuar")
            
    elif opcion=="salir":
        break
    
    else:
        print("Elige una respuesta valida")
        input("Pulsa enter para continuar")
