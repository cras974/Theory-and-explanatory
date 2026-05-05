#Autor: Miguel Ángel García Cortés
#Version 1.0

# Ejercicio 1

lista=[]
contador=0


while True:
    print("---------------------------------------")
    print("| 1) Añadir producto                  |")
    print("| 2) Mostrar productos                |")
    print("| 3) Eliminar producto por su nombre  |")
    print("| 4) Buscar producto por nombre       |")
    print("| 5) Contar productos en la cesta     |")
    print("| 6) Vaciar la cesta                  |")
    print("| 7) Salir del menu                   |")
    print("---------------------------------------")
    print(" ")
    opcion=input("Elige una opcion: ")
    
    if opcion == "1":
        producto=input("Dime que producto quieres añadir: ")
        existe=lista.count(producto)
        if existe <= 0:
            lista.append(producto)
            print("Añadido exitosamente")
        elif existe >= 1:
            print("El producto ya existe")
            
            
    elif opcion == "2":
        longitud=len(lista)
        
        if longitud >= 1:
            for i in lista:
                print (i," ",end="")
        else:
            print("La lista esta vacia")
            
        print(" ")
    
    elif opcion == "3":
        eliminar=input("Dime el nombre del producto a eliminar: ")
        existe=lista.count(eliminar)
        if existe > 0:
            lista.remove(eliminar)
            print("Eliminado exitosamente")
        elif existe <= 0:
            print("El producto no existe")
    
    elif opcion == "4":
        elemento=input("Dime el nombre del elemento a buscar: ")
        existe=lista.count(elemento)
        if existe <= 0:
            print("El elemento que buscas no existe")
        elif existe >= 1:
            print("El elemento esta en la cesta")
    
    elif opcion == "5":
        productos=len(lista)
        
        print(f"Actualmente hay un total de {productos} productos")
    
    elif opcion == "6":
        confirma=input("Estas seguro de eliminar toda la cesta?(s/n): ")
        if confirma == "s":
            productos=100
            while productos > 0:
                productos=len(lista)
                for i in lista:
                    lista.remove(i)
        
        elif confirma == "n":
            print("Accion cancelada")
        
        else:
            print("Pon s o n, vuelve a intentarlo")
                
    elif opcion == "7":
        break
    
    else:
        print("Opcion incorrecta")
        
print("Programa finalizado")
    