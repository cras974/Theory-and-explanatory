# 1) Añadir numero a la lista. Me pide un numero de la lista y lo añade al final.
# 2) Añadir numero de la lista en una posicion. Me pide un numero y una posicion y si la posicion existe en la lista lo añade a ella (la posicion se pide a partir de 1).
# 3) Longitud de la lista te muestra el numero de elementos de la lista.
# 4) Eliminar el ultimo numero. Muestra el ultimo numero de la lista y lo borra.
# 5) Eliminar un numero. Pide una posicion y si la posicion existe en la lista lo borra de ella (la posicion se pide a partir de 1).
# 6) Contar numeros. Te pide un numero y te dice cuantas apariciones hay en la lista.
# 7) Posiciones de un numero. Te pide un numero y te dice en que posiciones esta (contando desde 1).
# 8) Mostrar numeros: Muestra los numero de la lista.
# 9) Salir.
lista = []
while True:
    print("---------MENÚ-------------")
    print("")
    print("1) Añadir numero a la lista. ")
    print("2) Añadir numero a la lista en una posicion. ")
    print("3) Longitud de la lista. ")
    print("4) Eliminar el ultimo numero de la lista. ")
    print("5) Eliminar un numero de la lista. ")
    print("6) Contar cuantas veces aparece un elemento en la lista. ")
    print("7) Posiciones de un numero. ")
    print("8) Mostrar numero de la lista. ")
    print("9) Salir.")
    print("")
    print("")
    opcion = int(input("Introduce una opcion: "))

    if opcion == 1:
        numero = int(input("Introduce un numero: "))
        lista.append(numero)
    elif opcion == 2:
        numero = int(input("Introduce un numero: "))
        posicion = int(input("Introduce una posicion:(empieza a partir de 1) "))
        if posicion > len(lista):
            print("Posicion incorrecta")
        else:
            lista.insert(posicion -1,numero)
    elif opcion == 3:
        print("Longitud de la lista: %d" len(lista))
    elif opcion == 4:
        print(lista -1)
        lista.pop(-1)
        print(lista)
    elif opcion == 5:
        pos = int(input("Dime una posicion (empeczando por 1):"))
        if pos > len(lista):
            print("Posicion incorrecta")
        else:
            print("Posicion incorrecta")

    elif opcion == 6:
        num = int(input("Dime una posicion empezando por 1:"))
        print("El elemento es %d aparece %d de veces" % (num,lista.count(num)))


    elif opcion == 7:
        num=int(input("Dime un numero: "))
        indice_buscar=0
        print("Posiciones: ",end="")
        for indice in range(0,lista.count(num)):
            indice_buscar = lista.index(num,indice_buscar)
            indice_buscar+=1
            print(indice_buscar," ",end="")
        print()

    elif opcion == 8:
        for num in lista:
            print(num," ",end="")
        print()
    elif opcion == 9:
        break

    else:
        print("Opcion incorrecta")