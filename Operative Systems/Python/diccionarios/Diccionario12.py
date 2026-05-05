ciudades = {
    "Madrid": {
        "pais": "España",
        "poblacion_millones": 3.3,
        "superficie_km2": 604.3,
        "PIB_millones": 230000,
        "altitud_metros": 667,
        "temperatura_media": 15.5,
        "habitantes_por_km2": 5457,
        "costo_vida": 80,
        "industrias_principales": ["Turismo", "Finanzas", "Construcción"],
        "aeropuertos": ["Madrid-Barajas", "Torrejón"]
    },
    "Ciudad de México": {
        "pais": "México",
        "poblacion_millones": 9.2,
        "superficie_km2": 1485,
        "PIB_millones": 411000,
        "altitud_metros": 2240,
        "temperatura_media": 17.5,
        "habitantes_por_km2": 6198,
        "costo_vida": 70,
        "industrias_principales": ["Manufactura", "Finanzas", "Telecomunicaciones", "Turismo"],
        "aeropuertos": ["Aeropuerto Internacional Benito Juárez"]
    },
    "Tokio": {
        "pais": "Japón",
        "poblacion_millones": 14.0,
        "superficie_km2": 2194,
        "PIB_millones": 1690000,
        "altitud_metros": 40,
        "temperatura_media": 16.0,
        "habitantes_por_km2": 6380,
        "costo_vida": 95,
        "industrias_principales": ["Tecnología", "Automotriz", "Turismo"],
        "aeropuertos": ["Narita", "Haneda"]
    },
    "Nueva York": {
        "pais": "EE.UU.",
        "poblacion_millones": 8.4,
        "superficie_km2": 783.8,
        "PIB_millones": 1710000,
        "altitud_metros": 10,
        "temperatura_media": 12.7,
        "habitantes_por_km2": 10720,
        "costo_vida": 100,
        "industrias_principales": ["Finanzas", "Medios de comunicación", "Turismo", "Tecnología"],
        "aeropuertos": ["JFK", "LaGuardia", "Newark"]
    },
    "Londres": {
        "pais": "Reino Unido",
        "poblacion_millones": 8.9,
        "superficie_km2": 1572,
        "PIB_millones": 700000,
        "altitud_metros": 11,
        "temperatura_media": 11.3,
        "habitantes_por_km2": 5663,
        "costo_vida": 90,
        "industrias_principales": ["Finanzas", "Turismo", "Tecnología", "Comercio"],
        "aeropuertos": ["Heathrow", "Gatwick", "Stansted"]
    },
    "Berlín": {
        "pais": "Alemania",
        "poblacion_millones": 3.7,
        "superficie_km2": 891.8,
        "PIB_millones": 153000,
        "altitud_metros": 34,
        "temperatura_media": 10.5,
        "habitantes_por_km2": 4150,
        "costo_vida": 75,
        "industrias_principales": ["Tecnología", "Medios de comunicación", "Turismo", "Educación", "Extra"],
        "aeropuertos": ["Berlín-Brandeburgo"]
    }
}

import os

os.system("cls")

print("1️⃣ ¿Cuál es la ciudad con más industrias principales y cuántas tiene?")

print ("")

max_industria=0
ciudad = ""

for nombre in ciudades:
    num = len(ciudades[nombre]["industrias_principales"])
    
    if num > max_industria:
        max_industria = num
        ciudad = nombre
        
print(f"La ciudad con mas industrias es {ciudad} con {max_industria} industrias")

print ("")

print("2️⃣ ¿Qué porcentaje del PIB total representa cada ciudad?")

print ("")

total_pib = 0

for nombre in ciudades:
    total_pib = total_pib + ciudades[nombre]["PIB_millones"]
    
print (f"{total_pib}")

for nombre in ciudades:
    
    pib = ciudades[nombre]["PIB_millones"]
    porcentaje = (pib / total_pib) * 100
    print (f"{nombre} : {round(porcentaje)}% del pib total")
    

max_habit=0

for nombre in ciudades:
    habitantes = ciudades[nombre]["habitantes_por_km2"]

    if habitantes > max_habit:
        max_habit = habitantes
        ciudad = nombre

print("Ciudad con maximos habitantes", ciudad)

min_temp = 100


for nombre in ciudades:
    temp = ciudades[nombre]["temperatura_media"]

    if temp < min_temp:
        min_temp = temp
        ciudad = nombre

print("Ciudad con minima temperatura", ciudad)


print("7️⃣ Si se agregara un aeropuerto a cada ciudad que tenga menos de 2, ¿cuántas ciudades tendrían al menos 2 aeropuertos?")

contador = 0

for nombre in ciudades:
    aeropuertos = len(ciudades[nombre]["aeropuertos"])
    aeropuertos = aeropuertos + 1
    if aeropuertos >= 2:
        ciudad = nombre
        print(f"{nombre}")
        contador = contador + 1

print (f"{contador} hay ciudades con esos aeropuertos")