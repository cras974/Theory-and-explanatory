## 👤 Miguel Ángel García Cortés


<b>

## 🟢 Nivel 1 – Fundamentos: imágenes y contenedores

---

1️⃣ Ejercicio 1.1 – Primer contacto con Alpine Linux Descarga y ejecuta un contenedor de Alpine Linux. 

![pull](image-19.png)

Comprueba su tamaño, entra en modo interactivo y muestra la versión del sistema.

![version](image-20.png)
![peso](image-21.png)

---

2️⃣ Ejercicio 1.2 – Comprobando BusyBox Busca en Docker Hub la imagen oficial de BusyBox, descárgala, ejecútala y verifica qué comandos básicos tiene disponibles.

![oficial](image-22.png)

![pull](image-23.png)

![comandos](image-24.png)

---

3️⃣ Ejercicio 1.3 – Contenedor CentOS Descarga la imagen oficial de CentOS y crea un contenedor que permanezca activo.

![instalacion](image-26.png)

Verifica su versión y deténlo

![version](image-27.png)

![stop](image-28.png)

---

4️⃣ Ejercicio 1.4 – Explorando contenedores Lista todos los contenedores (en ejecución o detenidos), inspecciona uno para ver su dirección IP interna, y elimina aquellos que ya no necesites.

![listar](image-29.png)

![red](image-30.png)

![eliminado](image-31.png)

---

5️⃣ Ejercicio 1.5 – Información del sistema Docker Muestra información detallada de tu instalación Docker (versiones, almacenamiento, redes, etc.) y localiza el directorio donde se guardan las imágenes.

![version](image-32.png)

![ruta](image-33.png)

---

## ⚪ Nivel 2 – Redes docker

---

6️⃣ Ejercicio 2.1 – Creando una red personalizada Crea una red llamada red_lab y lanza en ella tres contenedores de diferentes distribuciones pequeñas (alpine, busybox, centos).

![crear_red](image-34.png)

![dockers](image-35.png)

Comprueba que pueden hacerse ping entre sí por nombre.

![pines](image-36.png)

---

7️⃣ Ejercicio 2.2 – Un contenedor en dos redes Crea una segunda red llamada red_extra y conecta uno de los contenedores anteriores a ambas redes.

Comprueba su configuración de red interna.

![red_extra](image-37.png)

![conectadoalpine](image-38.png)

![red_extra_inspect](image-39.png)

---

8️⃣ Ejercicio 2.3 – Servidor HTTP temporal Dentro de un contenedor python:3-alpine, inicia un servidor web con python3 -m http.server 8080 y accede a él desde otro contenedor de la misma red usando curl.

![server](image-40.png)

![conexion](image-41.png)

---

## 🔵 Nivel 3 – Volúmenes y persistencia

---

9️⃣Ejercicio 3.1 – Volumen compartido entre contenedores.

Crea un volumen llamado compartido y monta dicho volumen en dos contenedores distintos (alpine y busybox).

![creacion  y entrada](image-42.png)

Guarda un archivo en uno y verifica que aparece en el otro.

![prueba](image-43.png)

---

1️⃣0️⃣Ejercicio 3.2 – Volumen persistente con Alpine Lanza un contenedor alpine montando un volumen llamado vol_asir en la carpeta /datos. 

Dentro del contenedor crea un archivo llamado mensaje.txt con el texto Hola ASIR. 

Elimina el contenedor y lanza otro nuevo utilizando el mismo volumen. 

Comprueba que el archivo mensaje.txt sigue existiendo y conserva su contenido original.

![archivo.txt](image-44.png)

---

## ⚫ Nivel 4 – Mantenimiento y limpieza

---


1️⃣1️⃣Ejercicio 4.1 – Limpieza y diagnóstico del entorno Lista imágenes, contenedores, volúmenes y redes. 

Elimina los elementos que no estén en uso. 

Comprueba cuánto espacio ocupa Docker en tu sistema antes y después.

![def](image-45.png)

![prune](image-46.png)

![post-prune](image-47.png)