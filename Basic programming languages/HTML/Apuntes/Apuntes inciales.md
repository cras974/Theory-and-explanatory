# :question: **Apuntes inciales HTML**

<br>

<center><img src="images.png"></center>

<br>

:bust_in_silhouette: **Miguel Ángel García Cortés**

:date: **9/09/2025**

***Los - dentro de las etiquetas se deben ignorar <-ejemplo>***

---

El HTML es el lenguaje que usan las **web** **W3C son los diseñadores del estandar** de HTML y otros lenguajes de programación.

### :eyes: --> [Web W3C para practicar HTML](https://www.w3schools.com/html/default.asp) *//Recomendado usar el ingles//*

> Esta página permite el uso de codigo online y ejecutarlo sin necesidad de tenerlo de forma local.

Para abrir un codigo de HTML en forma de página y poder visualizarlo debemos poner en la extension .html, para volver a editarlo .txt 

// *(En caso del bloc de notas)*


>  ***:heavy_minus_sign: Se recomiendo usar el firefox (Interpreta mejor xml, html)***

El codigo HTML es visualizado por los navegadores ya que es un lenguaje ***INTERPRETADO***

// *HTML significa: Hyper Text Markup Language, se refiere a un lenguaje que tiene diversas formas como : <-etiqueta>*

## :exclamation:Ejemplo de etiqueta

> La etiqueta de apertura será : <> y la de cierre </>.

### **Etiqueta <-h>**
<-h1> Buenas tarde <-/h1>
<h1> Buenas tardes </h1>
<-h3> Ejemplo h3 <-/h3>
<h3> Ejemplo h3 </h3>
<br>

> :arrow_forward: Para la eitqueta <-h>, tiene distintos tamaños de letras, que pueden llegar desde el :one: hasta el :seven:, empezando por :one: como el más grande  posible.

---
El lenguaje de HTML no distingue entre mayusculas y minusculas denominado como **NO** "Case sensitive"

**Se pueden poner multiples etiquetas de golpe, poniendo la etiqueta como por ejemplo p por 3 es decir etiqueta por numero**

Dentro del lenguaje HTML no debemos usar demasiados espacios ni enters, ya que no tendrán utilidad, hay que usar las etiquetas designadas para cada uno.

Hay algunas etiquetas que no van a necesitar cierre como puede ser <-br>

>*<-br> permite añadir saltos en blanco.*

 :bangbang:En el documento HTML siempre empezará con la etiqueta 
 
 <-!DOCTYPE html>    

 <-html>      *// Es la base*

 <-head>    *// Cabezera*

 <-/head>  

 <-body>    *// Donde irá todo el contenido*

 <-/body>  

 <-/html>  *//Importante cerrar*

### :arrow_forward:  **Etiqueta <-p>**

**Esta etiqueta es usada para los parrafos**

// *Entre dos etiquetas <-p> genera una separación automatica*

**EJEMPLO**

<p> Hola, mi nombre es pepe
Hola, mi nombre es pepe
Hola, mi nombre es pepe</p> 

--- :arrow_down: --- *//Parrafos distintos*

<p>Hola, mi nombre es pepe</p>

---

### :notebook: Elementos de bloque

Estos elementos establecen un salto de linea propio, pero lo demás serán una forma de bloque, todo unido.

### :notebook_with_decorative_cover: Elementos de línea

Estos elementos van linea por linea, no forman un bloque conjunto.

## Ejercicio de ejemplo

--- :arrow_down: ---

*// Se debe abrir con .HTML*

[Ejercicio de bloc de notas](Ejemplo_bloc.txt)

## Formularios en HTML

--- :arrow_down: ---

Un formulario está compuesto por un conujunto de elementos de entrada de información. Permite al usuario introducir datos con el objetivo de enviarlos a un servidor para realizar algun tipo de proceso con ellos.

El ciclo de funcionamiento de un formulario es el siguiente:

 - 1 El usuario introduce los datos en los campos de entrada correspondientes.

 - 2 El usuario pulsa el boton de envio.

 - 3 El navegador valida las reglas asignadas a los campos de entrada.

 - 4 Si las reglas se cumplen, el navegador prepara los datos y los envia al destino indicado según el método de envío seleccionado.

 ### Atributos

- **<-form action="paginaservidor.php" method="post">**
<-/form>
*// El nombre del servidor y como se envian los datos.*

- **<-input type="text" name="nombre" >** *//Esto es para crear un bloque de texto, el nombre indica para que quieres que sea, el tipo para eso mismo.*

Antes del input puedes escribir texto para indicar.

Para indicar que el input sea obligatorio se puede usar:

- **required**

Para indicar el maximo de caracteres se puede usar:

- **maxlength="numero"**

Para indicar el minimo de carácteres se puede usar:

- **minlength="numero"**

Indica el tamaño de visualización.

- **size="7"**

Crea un texto dentro del bloque, para dar información extra, actua como informador unicamente.

- **placeholder="Introduzca su nombre"**

Indica un valor por defecto en el bloque de texto.

- **value="Pepe"**

Con el id puedes indicar que este elemento tendra un label.

**id="nombre del for del label"**

### Label

Es una etiqueta, con esto le creas un identificador al elemente.

**<-label for="minombre">Nombre:<-/label>**

 <br>

 ### type="password"

 Este tipo de input tiene otras características, se usa para contraseñas.

**<-label for="passw">Contraseña: <-/label> <br>
 <-input type="password" name="contrasena" id="passwd">**

 Por lo general deberían tener el atributo required y minlength también.


 ### type="number" 

 Esto se usa principalmente y unicamente para numeros.

**<-input type="number" name="edad">**

Tiene atributos especificos

**min="numero minimo"**

**max="numero máximo"**

Con step puedes pedir saltos de x numeros.

Es decir, numero + X

**step="numero salto"**

### Boton de envio

**<-input type="submit" value="ENVIAR">**

**<-input type="reset" value="Restablecer">**

## Párrafos de texto

Para poner textos más grandes usaremos cuadros de texto.

<-textarea id="texto" name="descricpion_larga" rows="numero" cols="numero"><-/textarea>

El atributo cols, y rows permite aumentar el tamaño de visualización del cuadro.
### Date

Para poner una fecha, o fecha de nacimiento se usa **<-type="date" name="Fecha de nacimiento">**

### Fieldset

Para poner una caja alrededor del formulario existe la etiqueta.

**<-fieldset>** entre los inputs.

Se puede poner un titulo a la caja con la etiqueta **<-legend>** dejabo de fieldset.

### Crear desplegables

<-select name="coches">
    <-option value="audi">Audi<-/option>
    <-option value="toyota">Toyota<-/option>
<-/select>

Si pones el atributo <b> multiple </b> dejará elegir varias opciones

Si ponemos el atributo <b> size="cantidad" </b> en el select, se mostrará la cantidad elegida.

Para poner categorías dentro de los grupos podemos poner el atributo

<b>
<-select name="coches"> <br>
    <-optgroup label="Coches suecos"> <br>
        <-option value="audi">Audi<-/option> <br>
        <-option value="toyota">Jaguar<-/option> <br>
    <-optgroup label="Coches Japoneses"> <br>
        <-option value="audi">Mitsubishi<-/option> <br>
        <-option value="toyota">Toyota<-/option> <br>
<-/select><br>
</b>
<br>

El atributo value, es lo que envia a la página, y el texto entre >texto< es lo que se muestra.

## Checkbox

Si quiero poner una caja con checkbox simplemente

<-input type="checkbox" id="check" name="notif" value="Que hace"> <br>
<-label for=check> Quiero recibir lo que haga <-/label> <br>

Si quiero que salga marcado ponemos el atributo **checked**
### Crear listas seleccionables

**<-input type="radio" id="html" name="fav-language" value="HTML">**
**<-label for="html">HTML<-/label>**

**<-input type="radio" id="JS" name="fav-language" value="JS">**
**<-label for="JS">JS<-/label>**

Si tienen el mismo valor en "name", se vuelven excluyentes, es decir no se pueden seleccionar más de uno con el mismo valor en name.

Si quieres que uno este marcado por defecto puedes poner el atributo 

<br>


## Ediciones de texto

Para poner en negrita un texto en html usaremos la etiqueta **<-b>**

Para poner el texto en cursiva usaremos la etiqueta **<-i>**

Para crear superindices usaremos la etiqueta **<-sup>numero<-/sup>**

## Tablas

Debemos usar la estructura

thead

tbody

tfoot
