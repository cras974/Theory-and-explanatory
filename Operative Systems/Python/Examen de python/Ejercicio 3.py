#Autor: Miguel Ángel García Cortés
#Version 1.0

# Ejercicio 3

peso=int(input("Dime el peso del paquete en gramos: "))
destino=int(input("Dime el destino del 1 al 5: "))

if peso > 8000:
    print("Peso del paquete excedido")
    exit(True)

if destino == 1:
    total=peso*0.015
    total=total+5
    print("El precio total ha sido de: ",total)
    print("El paquete ha sido enviado a Andalucía")
    print("Recuerde que se han añadido a su tarifa 5€ de envio.")
    
elif destino == 2:
    total=peso*0.020
    total=total+5
    print("El precio total ha sido de: ",total)
    print("El paquete ha sido enviado a Comunidad de Madrid")
    print("Recuerde que se han añadido a su tarifa 5€ de envio.")

elif destino == 3:
    total=peso*0.018
    total=total+5
    print("El precio total ha sido de: ",total)
    print("El paquete ha sido enviado a Cataluña")
    print("Recuerde que se han añadido a su tarifa 5€ de envio.")

elif destino == 4:
    total=peso*0.017
    total=total+5
    print("El precio total ha sido de: ",total)
    print("El paquete ha sido enviado a Comunidad Valenciana")
    print("Recuerde que se han añadido a su tarifa 5€ de envio.")
   
elif destino == 5:
    total=peso*0.016
    total=total+5
    print("El precio total ha sido de: ",total)
    print("El paquete ha sido enviado a Galicia")
    print("Recuerde que se han añadido a su tarifa 5€ de envio.")

else:
    print("Usted ha introducido un destino incorrecto")