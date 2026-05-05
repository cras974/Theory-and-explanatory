# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:Escribir un algoritmo para calcular la nota final de un estudiante, 
# considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

correctas=int(input("Cuantas respuestas correctas ha tenido: "))
incorrectas=int(input("Cuantas respuestas incorrectas ha tenido: "))
nula=int(input("Cuantas respuestas sin contestar ha tenido: "))

print("La puntuacion del alumno es: ", correctas*5+nula*0-incorrectas*1)