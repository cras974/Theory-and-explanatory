# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Una persona adquirió un producto para pagar en 20 meses. 
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.


pago=10

for mes in range(2,21):
    print("Es el mes: ", mes)
    pago=pago*2
    total=pago/2+pago

print("El pago total es: ",total+10)