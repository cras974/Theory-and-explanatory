# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. 
# Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, 
# considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

preciouva=int(input("A cuento esta el precio del kilo de uva: "))

tipo=input("El tipo de la uva es A o B: ")
tamano=int(input("El tamaño es 1 o 2: "))

cantidad=int(input("Cuantas uvas tienes: "))

if tamano == 1 and tipo == "A":
    print("El beneficio total es: ", cantidad*preciouva+20*cantidad)

elif tamano == 2 and tipo == "A":
    print("El beneficio total es: ", cantidad*preciouva+30*cantidad)
    
elif tamano == 1 and tipo == "B":
    print("El beneficio total es: ", cantidad*preciouva+(-30)*cantidad)

elif tamano == 2 and tipo == "B":
    print("El beneficio total es: ", cantidad*preciouva+(-50)*cantidad)