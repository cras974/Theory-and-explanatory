# EJERCICIOS DE REDES DOCKER

### ✅ Ejercicio 1 — Crear tres redes Docker personalizadas

<b>

#### Crea tres redes Docker, cada una con su propia IP y rango.

🔵 Red A — redA
Subred: 10.10.10.0/24
Gateway: 10.10.10.1
Rango: 10.10.10.50 – 10.10.10.60
🟢 Red B — redB
Subred: 20.20.20.0/24
Gateway: 20.20.20.1
Rango: 20.20.20.100 – 20.20.20.120
🔴 Red C — redC
Subred: 30.30.30.0/24
Gateway: 30.30.30.1
Rango: 30.30.30.150 – 30.30.30.160

</b>
<br>
<b>

Creacion de redes.

![creacion](image.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

Red A

![REDAinsp](image-1.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

Red B

![redbinsp](image-2.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

Red C

![redcinsp](image-3.png)

✅ Ejercicio 2 — Lanzar DOS contenedores en cada red
(todos distintos)
Debes usar SEIS contenedores, todos con un sistema operativo diferente.

✅ En redA deben lanzarse:
Contenedor Imagen SO
a1 ubuntu Ubuntu
a2 fedora Fedora

✅ En redB deben lanzarse:
Contenedor Imagen SO
b1 debian Debian
b2 centos:7 CentOS

✅ En redC deben lanzarse:
Contenedor Imagen SO
c1 alpine Alpine
c2 rockylinux Rocky Linux

![dockers](image-4.png)

![rocky](image-5.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

✅ Ejercicio 3 — Crear un contenedor conectado a las TRES
redes
Crea un contenedor llamado multired3 basado en Fedora que debe pertenecer a:
redA
redB
redC
Tareas:
Lanzarlo inicialmente en redA.
Conectarlo después a redB y redC.
Verificar 3 interfaces con ip addr.

![multired3](image-6.png)

Instalamos los paquetes de red

![paquetes](image-7.png)

Ip address

![ip addr](image-8.png)

<br><br><br><br><br><br><br>

✅ Ejercicio 4 — Crear un contenedor conectado a DOS
redes
Crea un contenedor llamado multired2 basado en distroless o busybox que debe pertenecer
a:
redA
redC
Tareas:
Implantación de Sistemas Operativos 1º ASIR
Profesora: Ana Fuentes 2/3
Inicialmente lanzarlo en redC.
Añadirlo a redA.
Verificar interfaces: 2 direcciones IP

![creacionmulti2](image-9.png)

![conexionesmulti2](image-10.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

✅ Ejercicio 5 — Comprobación de conectividad
✅ 5.1 Comunicaciones dentro de la misma red
a1 ↔ a2
b1 ↔ b2
c1 ↔ c2

![a1,b1](image-11.png)
![c1](image-12.png)

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

✅ 5.2 Comunicaciones de los contenedores multired
🟦 multired3 (opensuse) debe alcanzar:
a1 (Ubuntu), a2 (Fedora)
![a1,a2](image-13.png)
b1 (Debian), b2 (CentOS)
![b1,b2](image-14.png)
c1 (Alpine), c2 (Rocky)
![c1,c2](image-15.png)

🟧 multired2 (busybox/distroless) debe alcanzar solo:
a1, a2 (por redA)
![a1,a2,m2](image-16.png)
c1, c2 (por redC)
![c1,c2,m2](image-17.png)
<br><br>
✅ 5.3 Aislamiento esperado
a1 NO debe alcanzar b1
b2 NO debe alcanzar c1
a2 NO debe alcanzar c2

![aislamiento](image-18.png)

