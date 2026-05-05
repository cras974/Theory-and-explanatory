# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

pedido=-1
total=0
media=0
contador=0

while pedido != 0:
    print("Introduce 0 para salir.")
    pedido=int(input("Introduce un numero: "))
    contador=contador+1
    total=pedido+total
    media=total/contador
    print("La suma de los numeros es: ", total)
    print("La media de los numeros es: ", media)