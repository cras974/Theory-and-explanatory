#Realiza un programa que muestre la nota madie de cada alumno
#Indica que alumno tiene la media mas alta

notas = {
    "Ana" : [7,8,9],
    "Luis": [5,6,7],
    "Marta":[10,9,8]
}

mejor_media=0
mejor_alumno = ""

for c,v in notas.items():
    media=sum(v)/len(v)
    print(f"{c} La nota media es: {media}")
    
    if media > mejor_media:
        mejor_media = media
        mejor_alumno = c

print(f"El mejor alumno es {mejor_alumno} con {mejor_media}")
