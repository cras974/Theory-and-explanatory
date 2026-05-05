# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:

'''
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. 
El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:


Zona	Ubicación	        Costo/gramo
1	    América del Norte	24.00 euros
2	    América Central	    20.00 euros
3	    América del Sur	    21.00 euros
4	    Europa	            10.00 euros
5	    Asia	            18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. 
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
'''

peso=int(input("Cuanto pesa el paquete en gramos: "))
dir=input("A donde va el paquete, pon el numero de zona: ")

if peso > 5000:
    print("El peso excede el limite indicado, lo siento.")

elif dir == "1" and peso < 5000:
    print("El precio es: ",peso*24,"€")
    
elif dir == "2" and peso < 5000:
    print("El precio es: ",peso*20,"€")
    
elif dir == "3" and peso < 5000:
    print("El precio es: ",peso*21 ,"€")
    
elif dir == "4" and peso < 5000:
    print("El precio es: ",peso*10 ,"€")
    
elif dir == "5" and peso < 5000:
    print("El precio es: ",peso*18 ,"€")
    
else:
    print("Vuelva a introducir los datos correctamente")

print("Fin del programa")