# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1 = int(input("Dime un cateto: "))
cateto2 = int(input("Dime el otro cateto: "))

hipotenusa = math.sqrt(cateto1**2+cateto2**2)

print ("La hipotenusa es", hipotenusa)