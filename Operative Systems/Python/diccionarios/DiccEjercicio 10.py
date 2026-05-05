# Crea un programa de Login que compruebe el usuario y contraseña en el diccionario siguiente:

usuarios = {  
      "iperurena": {  
          "nombre": "Iñaki",  
		  "apellido": "Perurena",  
		  "password": "123123"  
	  },  
	  "fmuguruza": {  
	       "nombre": "Fermín",  
		  "apellido": "Muguruza",  
		  "password": "654321"  
	  },  
	  "aolaizola": {  
	       "nombre": "Aimar",  
		  "apellido": "Olaizola",  
		  "password": "123456"  
	  }  
    }

login_usuario = input("Dime tu nombre de usuario: ")
login_password = input("Dime tu contraseña: ")

if login_usuario in usuarios:
    if usuarios[login_usuario]["password"] == login_password:
        datos = usuarios[login_usuario]
        print(f"Bienvenido/a {datos['nombre']} {datos['apellido']}. Acceso concedido.")
    else:
        print("Contraseña incorrecta.")
else:
    print("El usuario no existe.")