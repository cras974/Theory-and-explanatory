# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. 
# Por ejemplo 5! = 1x2x3x4x5=120).


numero = int(input("Pon un número: "))
factorial = 1
contador = 1


while contador <= numero:
    factorial = factorial * contador
    print("Multiplicando por", contador, "el total es:", factorial)
    contador = contador + 1
    
print("El resultadol es:", factorial)