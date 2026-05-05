# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción:Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

dia=int(input("Que día es hoy (Del 1 al 7): "))

if dia == 1 :
    print("Hoy es lunes")
elif dia == 2:
    print("Hoy es martes")
elif dia == 3:
    print("Hoy es miercoles")
elif dia == 4:
    print("Hoy es jueves")
elif dia == 5:
    print("Hoy es viernes")
elif dia == 6:
    print("Hoy es sabado")
elif dia == 7:
    print("Hoy es domingo")
else:
    print("Introduce un dia valido, del 1 al 7")

print("Fin del programa")