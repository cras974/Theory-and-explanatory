#Escribe distintas funciones en en Python que lean el fichero json libreria.json con datos de nuestra 
#librería y muestre la siguiente información:

#¿Cuántos libros hay en la librería?

#Recibe un límite inferior y superior para el precio y muestra todos los libros cuyo precio esta en ese intervalo.

#Recibe una cadena por teclado, y muestra el título y el año de publicación de los libros cuyo título 
#empiece por la cadena introducida.

#Devuelve todos los títulos de los libros con la lista de sus autores.

import json

import os

os.system("cls")


with open("libreria.json", "r", encoding="utf-8") as archivo:
    
    libreria = json.load(archivo)
    
    def libros():
        
        lista_libros = libreria["bookstore"]["book"]
        
        contador = 0
        
        for i in lista_libros:
            contador += 1

libros()