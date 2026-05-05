import os

os.system("cls")

lista = []

while True:
    
    op = input("Escribe salir para finalizar | Introduce enter para seguir: ")
    
    if op == "salir":
        break
    
    else:
        num=int(input("Dime el numero a añadir a la lista: "))
        lista.append(num)

maximo=0
minimo=0

def calcularMaxMin():
    maximo=max(lista)
    minimo=min(lista)
    
    print(f"El maximo es: {maximo} \nEl minimo es: {minimo}")

calcularMaxMin()