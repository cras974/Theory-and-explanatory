import json

import os

os.system("cls")

with open("usuarios.json", "r", encoding="utf-8") as archivo:
    diccionario = json.load(archivo)

#1)

activo = 0
inactivo = 0

usuarios = []

for i in diccionario:
    act = i["activo"]
    print(i["activo"])
    usuarios.append(act)
    
for i in usuarios:
    if i == "True":
        activo = activo + 1
    elif i == "False":
        inactivo = inactivo +1

print (f"Hay {activo} usuarios activos")
print (f"Hay {inactivo} usuarios inactivos")

#2) Calcular el gasto total de cada usuario activo y mostrar un ranking
#   descendente por gasto total
