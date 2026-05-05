#Escribir una función que elabora un diccionario con las notas de las asignaturas 
#de un curso, donde preguntaras las materias, 
#que serán las claves, y las notas, que serán los valores. También preguntará 
#una cadena con el nombre de un color (por ejemplo, "red", "blue", "green", etc. 
#o utilizar códigos hexadecimales para definir los colores por ejemplo, "#FF0000" para rojo). 
#El programa debe devolver un diagrama de barras de las notas en el color dado.

import matplotlib.pyplot as plt

curso = {}

def diccionario():
    
    materia = input("Dime la materia: ")
    nota = int(input("Dime la nota: "))
    curso[materia]=nota
    
while True:
    
    print("1) Añadir datos")
    print("2) Salir")
    print("")
    opcion = input("Dime una opcion: ")
    
    if opcion == "1":
        
        diccionario()
    
    elif opcion == "2":
        
        break
    
    else:
        print("Elige una opcion correcta")
    
x = []
y = []

for c,v in curso.items():
    x.append(c)
    y.append(v)

color=input("Dime que color quieres en ingles: ")

plt.bar(x, y, color=color)
plt.xlabel("Materia")
plt.ylabel("Notas")
plt.title("Curso")
plt.show()