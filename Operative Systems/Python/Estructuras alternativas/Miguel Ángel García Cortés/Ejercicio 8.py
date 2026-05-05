# Autor: Miguel Ángel García Cortés
# Versión: 1.0
# Descripción: Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’
# y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. 
# En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

nota=int(input("Dime una nota: "))
edad=int(input("Dime la edad: "))
sexo=input("Dime si es F, femenino, o M si es masculino: ")

if nota>=5 and edad>=18 and sexo=="F":
    print("Aceptada")
elif nota>=5 and edad>=18 and sexo=="M":
    print("Posible")
else:
    print("No aceptado")