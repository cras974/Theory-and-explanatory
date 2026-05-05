import os

os.system("cls")

vehiculos = {
    "Tesla Model 3": {
        "marca": "Tesla",
        "autonomia_km": 491,
        "precio_euros": 45000,
        "potencia_cv": 283,
        "ventas_2023": 120000,
        "paises_disponibles": ["EE.UU.", "España", "Alemania", "Francia", "Noruega"]
    },
    "Renault Zoe": {
        "marca": "Renault",
        "autonomia_km": 395,
        "precio_euros": 32000,
        "potencia_cv": 135,
        "ventas_2023": 48000,
        "paises_disponibles": ["Francia", "España", "Italia"]
    },
    "Volkswagen ID.4": {
        "marca": "Volkswagen",
        "autonomia_km": 520,
        "precio_euros": 50000,
        "potencia_cv": 204,
        "ventas_2023": 60000,
        "paises_disponibles": ["Alemania", "España", "EE.UU.", "Suecia"]
    },
    "Hyundai Ioniq 5": {
        "marca": "Hyundai",
        "autonomia_km": 481,
        "precio_euros": 47000,
        "potencia_cv": 217,
        "ventas_2023": 75000,
        "paises_disponibles": ["Corea del Sur", "EE.UU.", "España", "Alemania"]
    },
    "Nissan Leaf": {
        "marca": "Nissan",
        "autonomia_km": 385,
        "precio_euros": 31000,
        "potencia_cv": 147,
        "ventas_2023": 43000,
        "paises_disponibles": ["Japón", "España", "EE.UU."]
    },
    "BMW i4": {
        "marca": "BMW",
        "autonomia_km": 590,
        "precio_euros": 62000,
        "potencia_cv": 340,
        "ventas_2023": 30000,
        "paises_disponibles": ["Alemania", "EE.UU.", "España", "Francia"]
    },
    "Kia EV6": {
        "marca": "Kia",
        "autonomia_km": 528,
        "precio_euros": 49000,
        "potencia_cv": 229,
        "ventas_2023": 56000,
        "paises_disponibles": ["Corea del Sur", "EE.UU.", "España", "Italia", "Francia", "Alemania"]
    }
}

print("1) Mostrar la marca de cada modelo")
print("")

for coche in vehiculos.values():
    print(f"Marca: {coche["marca"]}")
    
print("")
print("----------------")
print("")

print("2) Crear una lista con los nombres de los modelos que contienen la palabra Model")
print("")

model = []

for modelo in vehiculos.keys():
    if "Model" in modelo:
        model.append(modelo)
    
for i in model:
    print (f"El modelo {i} contiene la palabra ""Model""")
    
        
print("")
print("----------------")
print("")

print("3) Calcular el procentaje de ventas que representa cada coche respecto al total")
print("")

valor_total=0
for coche in vehiculos.values():
    valor_total= valor_total + int((coche["ventas_2023"]))

print("El conjunto de ventas es: ",valor_total)

n = 0

for coche in vehiculos.values():
    porcentaje=int((coche["ventas_2023"])) / valor_total * 100
    n= n +1
    print (f"El coche {n} tiene {round(porcentaje)}%")

print("----------------")
print("")

print("4) Que coche está disponible en mas paises y mostrar cuantos")
print("")

n2 = 0

max_paises = 0
cochepais = 0

for coche in vehiculos.values():
    paises = len(coche["paises_disponibles"])
    n2= n2 +1
    if max_paises < paises:
        max_paises = paises
        cochepais = n2
        
print (f"El coche {cochepais} tiene {max_paises} paises")


print("----------------")
print("")

print("5) Calcular el nuevo precio si todos suben un 10% y mostrar solo lo que supere 50000€")
print("")

n3= 0

for coche in vehiculos.values():
    valornuevos = coche["precio_euros"] + coche["precio_euros"]* 0.10
    n3= n3 +1
    if valornuevos > 50000:
        print (f"El coche{n3} tiene un valor de {round(valornuevos)}")