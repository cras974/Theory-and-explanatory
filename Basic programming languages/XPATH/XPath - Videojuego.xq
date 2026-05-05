(:
Tomando como fichero de entrada el documento XML proporcionado en este enunciado en el que se recogen algunos de los videojuegos más vendidos de la historia, y utilizando BaseX como herramienta para comprobar el buen funcionamiento de las soluciones, crear las siguientes consultas XPath:

Mostrar todos los videojuegos.

/videojuegos/videojuego

Mostrar los títulos de todos los videojuegos.

//videojuego/titulo

Mostrar todos los títulos de videojuegos que contengan la letra "T".

Matches compara, la 't' indica que tenga t donde sea, la i indica que da igual si
es mayuscula o minuscula, en titulo

//videojuego[matches(titulo, 't', 'i')]/titulo

Mostrar todos los títulos de videojuego que se hayan publicado a partir del año 2000.

//videojuego[@anyo >= 2000]/titulo

:)