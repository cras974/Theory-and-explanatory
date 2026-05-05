# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.


numero = int(input("Dame un numero: "))

for mult in range(1, 11):
    multiplicacion = numero * mult
    print(mult, "x", numero, "=", multiplicacion)