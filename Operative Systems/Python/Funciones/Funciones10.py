#Escribir dos funciones que permitan calcular:

#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la 
#opción de convertir a segundos, convertir a horas,minutos y segundos o 
#salir del programa.

def C_seg(h,m,s):
    segundos = h * 3600 + m * 60 + s
    return segundos

def C_horas(s):
    hor = s // 3600
    seg = s - hor*3600
    min = seg // 60
    seg = seg - min*60
    return hor, min, seg

    
while True:
    print("1.- Convertir a segundos")
    print("2.- Convertir a H / M / S")
    print("3.- Salir del programa")
    print("---------------------------")
    opcion=int(input("Selecciona una opcion: "))
    
    if opcion == 1:
        horas = int(input("Dame las horas: "))
        min = int(input("Dame los minutos: "))
        seg = int(input("Dame los segundos: "))
        print(f"Son {C_seg(horas,min,seg)} seg")
    
    elif opcion == 2:
        segundos = int(input("Dame los segundos a convertir: "))
        print(f"Corresponde a: {C_horas(segundos)}")
    
    elif opcion == 3:
        print("Saliendo del menu")
        break
    
    else:
        print("Opcion incorrecta")