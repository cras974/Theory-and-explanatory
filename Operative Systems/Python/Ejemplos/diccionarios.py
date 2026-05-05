
import os

os.system("cls")

persona = {}

continuar = True

while continuar:
    clave=input("¿Que información quieres guardar?: ")
    valor=input("Dame el valor: ")
    persona[clave]=valor
    for c,v in persona.items():
        print (f"{c} Tiene el valor --> {v}")
    continuar = input("¿Quieres continuar? (s/n): ")
    if continuar == "s":
        continuar=True
    elif continuar == "n":
        continuar = False
    