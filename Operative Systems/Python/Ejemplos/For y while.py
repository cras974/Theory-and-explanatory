# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:Uso basico del for y while

# -------------- FOR -------------------
'''
for i in range(2,11,3):         #Empieza en el 2, llega hasta el 10, porque empieza siempre en 1 menos (0 por defecto), y realiza saltos de 3 en 3
    print(f"Iteracion {i}")
    
'''

'''

for i in "Python":
    print (f"{1}")
    
'''

# -------------- WHILE -------------------

'''

#Pedir contraeña

contrasena = "asir"
clave = input("Dime la contraseña: ")

while clave != contrasena:
    
    print("Clave incorrecta")
    respuesta = input("Quieres continuar? (s/n) : ")
    
    if respuesta == "n":
        break
    
    clave = input("Incorrecto, dime la contraseña: ")

if clave == contrasena:
    print("Correcto, login exitoso")

print("Programa finalizado")

'''

import os

os.system("cls")

cont = 0

num = 1

maximo=int(input("Hasta que numero quieres llegar: "))

while num < maximo:
    if num % 2 == 0:
        print ("Numero: ",num)
        num = num+1
        cont= cont+1
    else:
        num = num+1
    
print("El numero total de pares es: ",cont)