# Comandos de dockers

## IMAGENES Y GENERAL

- Para todos los comandos usaremos docker

- Para listar los dockers que tenemos: docker images 

- Para las busquedas de imagenes: docker search NOMBRE_IMAGEN

- Para instalar algo: docker pull NOMBRE:VERSION

- Para eliminar una imagen: docker rmi NOMBRE_IMAGEN

- Para forzar eliminar una imagen: docker rmi -f NOMBRE_IMAGEN


## CONTENEDORES

- Para crear un contenedor usable: docker run -it --name NOMBRE_QUEREMOS NOMBRE_IMAGEN:VERSION TERMINAL(Por defecto pondremos bash.)

- Si queremos instalarlo y dejarlo en segundo plano sustituimos -it por -d

- Para indicar un puerto ponemos al final PUERTO_QUEREMOS:PUERTO_USA

- Ejemplo: docker run -d --name mi-nginx -p 8080:80 nginx

- Para ver los contenedores funcionando: docker ps

- Para ver los dockers creados: docker ps -a

- Eliminar un docker: docker rm NOMBRE/ID

- Para arrancar un docker pondremos: docker start NOMBRE/ID

- Para parar un docker: docker stop NOMBRE/ID

- Para forzar parar un docker: docker stop -f NOMBRE/ID

- Para entrar a un docker encendido y creado: docker exec -it NOMBRE TERMINAL(Bash por defecto)

- Para lanzar comandos en un docker desde fuera pondremos: docker exec NOMBRE COMANDO

- Para inspeccionar un docker: docker inspect NOMBRE

## MAPEO DE VOLUMENES

- DEBEMOS ESTAR EN LA CARPETA DONDE ESTA EL ARCHIVO QUE QUEREMOS METER AL LINUX

- Para mapear un volumen añadimos a: docker run -d --name mi-nginx -p 8080:80 nginx | añadimos | -v RUTA_WINDOWS:LA_RUTA_DEL_LINUX

- EJEMPLO: docker run -d --name web-nginx -p 9000:80 -v C:\Users\migue\Desktop\volumen_nginx:/usr/share/nginx/html nginx

APACHE
/usr/local/apache2/htdocs

## CREACION DE REDES

- Crear red: docker network create (--subnet=IP/MASCARA --ip-range=RANGOMAX --gateway=PUERTA) NOMBRE

- Asignar dockers a redes: docker run -d --name u1 --network red_asir ubuntu sleep infinity

- Sleep infinity, indica que no se apague la maquina sola y se mantenga Up.

- Para conocer nuestra ip: getent hosts NOMBREHOST

- Paquete de ip propias: iproute2

- Paquetes de red basicos: docker exec -it f1 bash -lc "yum update && yum install -y iputils-ping dnsutils curl"

- Para ver la red: docker network ls

- Para ver los contenedores dentro de una red: docker network inspect NOMBRE_RED

- Para añadir un docker a una red: docker network connect RED MAQUINA

- Para eliminar un docker de una red: docker network rm RED MAQUINA

- Eliminar una red: docker network rm NOMBRE_RED

- Crear un docker con red: docker run -d --name f2 --network red20-rango48 --ip=20.20.20.55 fedora sleep infinity