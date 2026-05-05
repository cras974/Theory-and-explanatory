#Y realiza un programa que muestre las siguientes informaciones:
# - Muestra el nombre y el año de la película
# - Muestra los actores que trabajan en la película.
# - Muestra la puntuación media de la película

import os

os.system("cls")

pelicula={
		"title": "Nyckeln till frihet",
		"year": "1994",
		"genres": [
			"Crime",
			"Drama"
		],
		"ratings": [8, 8, 6, 10, 2, 3, 4, 5, 4, 9, 3, 9, 6, 10, 4, 8, 10, 1, 2, 8, 1, 9, 5, 4, 4, 2, 4, 6, 9, 10],
		"duration": "PT142M",
		"releaseDate": "1995-03-03",
		"originalTitle": "The Shawshank Redemption",
		"storyline": "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red.                Written by\nJ-S-Golden",
		"actors": [
			"Tim Robbins",
			"Morgan Freeman",
			"Bob Gunton"
		],
		"posterurl": ""
	}

print (f" El titulo de la pelicula es: {pelicula.get("title")}")
print (f" El año de la pelicula es: {pelicula.get("year")}")

for a in pelicula.get("actors"):
    print (f" El actor: {a} participa")

media = []

for i in pelicula.get("ratings"):
    media.append(i)
    
print (f" La nota media es: {sum(media)/len(media)}")

# Otra manera es:

# print (f"Puntuacion media es: {sum(pelicula["ratings"])/len(pelicula["ratings"])}")