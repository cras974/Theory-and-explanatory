# :warning: Apuntes CSS (Cascade Style Sheets)

<b> Valores y unidades en CSS </b>

Los valores numéricos se pueden aplicar postivos o negativos, si tiene decimales se usa el . como separador decimal.

Podemos tener unidades absolutas o relativas:

    Longitud: px (Absoluto)
              %  (Porcentaje)
              em  (Como el porcentaje pero en unidades)

---

###  🚩 <b>Valores importantes</b>

<b>Algunas propiedades son importantes.</b>

```CSS
*{
    margin 10px /*Indica los margenes de la hoja */

    padding 10px /*Indica el espacio del texto con los elementos*/
}

/*Para bordes*/

#Bordes{
    border-color: blue;
    border-width: 4px;
    border-style: solid;
}

/*Tablas con los bordes completos*/

td,th{
    border: 1px solid brown
}

table{
    border-collapse: collapse;
}

/*Tipos de letra*/

#Ejemplo_Tipo_Letra{
    font-style: italic; /*Letra cursiva*/
        font-weight: bolder; /*Letra negrita*/
}

```


---

## :exclamation: <b> SELECTORES </b>

###  🚩 <b>Selectores básicos</b>

#### 🏮<b> Universal: </b>

    Los selectores universales son reglas que 
    siempre son principales, se aplican a pesar 
    de que haya otras cosas, son las primeras, como *

```CSS
*{
    margin: 10px;
}
```

#### 🏮<b> De tipo: </b>

    Son todos los elementos de ese tipo, como h1,h2,p..

```CSS
h1{
    color: crimson;
    font-style: italic;
}
```

#### 🏮<b> De clase: </b>

    .nombre clase / Se identifica con class=nombre /

```CSS
.positivo{
    color: rgb(81, 245, 81);
    font-weight: bolder;
}
```

#### 🏮<b> De identificador: </b>

    #nombre identificador / Se identifica con id=nombre /

```CSS
#introduccion{
    border-color: blue;
    border-width: 4px;
    border-style: solid;
    padding: 1em;
}
```

#### 🏮<b> De atributo: </b>

    [atributo] Se aplica a todo lo que tenga ese atributo

```CSS
[type]{
background-color: greenyellow;
}
```

    elemento [atributo] Se aplica a los elementos con 
    ese atributo

```CSS
input[type]{
background-color: greenyellow;
}
```

    elemento [atributo="valor"] Se aplica a los elementos
    con ese atributo que tenga ese valor.

```CSS
input[type="number"]{
background-color: greenyellow;
}
```

#### 🏮<b> Agrupacion de selectores: </b>

```CSS

h2,h3,th,td{

}
```

###  🚩 <b>Combinadores</b>
<b>
Son selectores en los que se tiene en cuenta la relación entre elementos en la estructura jerarquica del documento

#### 🏮<b> Tipos </b>
---

    De hermanos                 A~B    

    A y B son hermanos

---
    De hijos                    A>B     

    B es hijo de A

---
    De hermananos adyacentes    A+B     

    A y B son hermanos y b está inmediatamente a continuación de A

---

    De descendientes            A B     

    B Es un descenciente de A, pero no necesariamente es hijo directo.

###  🚩 <b>Pseudoclases</b>

<b> Se añade como palabra clave a continuación de un selector convencional, creando un nuevo filtro de selección en función del estado del elemento o de los elementos filtrados por el selector.</b>

#### 🏮<b>Filtros</b>

    ⚡ :checked
    
    El elemento es activo por el usuario.

---

    ⚡ :first-child 
    
    El primer elemento de un grupo de elementos hermanos.

---

    ⚡ :first-of-type

    El primer elemento de un tipo de entre un grupo de elementos hermanos

---

    ⚡ :focus

    El elemento activo es el foco, y se le aplica.

---

    ⚡ :hover

    El cursor del ratón se encuentra sobre el elemento.

---

    ⚡ :last-child

    El ultimo elemento del grupo de elementos hermanos.

---

    ⚡ :last-of-type

    El ultimo elemento de un tipo de entre un grupo de elementos hermanos

---

    ⚡ :nth-child(Numero_Posicion)|(odd(Es impar))|(even(Es par))

    El numero que pongamos es el tendra el diseño, se tendrá en cuenta todos los hermanos para su posición.

---

    ⚡ :nth-of-type(Numero_posicion)

    Ponemos el numero de la posicion deseada, solo se tendra en cuenta los de su tipo.

---

    ⚡ :required

    Para los que tengan el atributo required.

---

###  🚩 <b>Pseudoclases</b>

Al igual que las pseudoclases se le añaden a los selectores, pero no para crear un nuevo nivel de filtrado, si no para seleccionar, partes más precisas del conjunto de elementos proporcionados por el selector.

#### 🏮 Tipos

```CSS
⚡ selector::pseudoelemento{propiedad:valor;}

    ::after

    /*Se aplica antes*/
```
Permit añadir contenido con el atributo content antes del elemento seleccionado.

```HTML
    <p id="Quijote"> En un lugar de la mancha </p>
 ```

```CSS

#Quijote::after{
    content:"SEGUIR LEYENDO"
}
```
---
    ⚡ ::before

    Se aplica despues
---
    ⚡ ::first-letter

    Se aplica solo a la primera letra
---
    ⚡ ::first-line
---
    ⚡ ::selection
    
    Permite modificar el estilo de la seleccion realizada con el ratón
---
    ⚡ ::

---

###  🚩 <b>Posicionamiento</b>

#### 🏮 Universal

```CSS
*{
    box-sizing: border-box;
    margin:0px
}
```
</b>
Con esto quitas el margen por defecto del navegador

#### 🏮 El modelo de cajas

La maquetacion en CSS se basa en el denominado "modelo de cajas".

Segun este concepto, todos los elementos se encuentran ubicados en un contenedor rectangular denominado ***caja***.

Estas cajas tienen un conjunto de propiedades básicas comunes que afectan directamente a su ubicación en la página y al espacio que ocupa.

Ejemplo de caja.

```CSS

body{
    margin: 0px;
}

#divInterior{
    background-color: orange;
    width: 100%;
    height: 100%;
}

#divExterior{
    width: 50%;
    height: 200px;
    margin: 0px;
    margin-left: 30px;
    padding: 10px;
    padding-bottom: 50px;
    border-width: 5px;
    border-style: solid;
    border-color: brown;
    background-color: rgb(250, 230, 120);
}
```
---
#### 🏮Margen exterior
Es el espacio vacio que se agrega al al elmento y que lo separa del resto de elementos circundantes. Su dimension se modifica con la propiedad margin.

```CSS
objeto{
    margin-top
    margin-left
    margin-right
    margin-bottom
}

```

---

#### 🏮Margen interior
 Es el espacio vacio que se agrega al elemento  y separa del borde a su contenido. Su dimension se modifica con la propiedad padding

```CSS

objeto{
    padding-bottom
    padding-left
    padding-right
    padding-top
}
```

---

#### 🏮El borde

Puede tener distintos tipos de relleno que se encuentra entre el margen interior y el margen exterior, se configura con la propiedad border y ocupa espacio, por lo que aumenta el espacio.

```CSS
objeto{
    border
    border-radius
    border-style
    border-width
    border-color
}
```

---

#### 🏮Ancho

Representa el ancho del espacio del contenedor que puede contener elementos. Se modifica con la propiedad ***width***

---

#### 🏮Alto

Representa el alto del espacio del contenedor que puede contener elementos. Se modifica con la propiedad ***height***

---

###  🚩 <b>Layout</b>

Primero, se debe diseñar en papel.

Diseñar de lo grande a lo pequeño.

Utiliza el inspector del navegador.

Probar en distintos navegadores y dispositivos.

#### 🏮Propiedad display

Display 

    1. inline : 
    
    Acepta margin (Solo en horizontal) y acepta padding.

    Ignora width y height.

    2. inline-block :

    Es igual pero no ignora width y height.

    3. block :

    Provoca un salto de linea tanto anterior como posterior.

    Por defecto ocupa toda la anchura.

    4. none :

    No deja espacio vacio.

La relación de valores de la propiedad display es muy extensa, pemitiendo incluso combinarlos. Se dividen en aquellos orientados a la visualización interna (Cómo se distribuyen los componentes dentro de la caja) y los orientados a la visualización externa (Cómo se comporta la caja en relación a los elementos que la rodean). 

Visualización externa: vista anteriormente (Block, display block, inline etc).

---

#### ⚠️ Visualización interna

Los valores mas utilizados para el tipo de visualización interna son los siguientes:

    1. Flex: Todo en el archivo css Posicionamiento > Display


    2. Grid:



---

#### 🏮Universal

Los margin estan fuera de la caja, y no va contado.

Debemos tener en cuenta que las cajas y margenes no superen el 100%

```CSS

*{
    box-sizing: border-box
    /*Hace que el border se incluya en el % de la caja*/
}
```

#### 🏮Centrado horizontal

- Elementos en linea
<br>
    - text-aling:center;
    (Alinea el contenido al centro)
<br>
- Elementos de bloque
<br>
    - margin:numpx numpx o auto auto o numpx auto;

    El primer valor es por arriba y por abajo y el otro por izquierda y derecha.

<br>

- Varios elementos en bloque en la misma fila.
<br>
    - display: inline-block;
<br>
    - text-aling: center;

#### 🏮Centrado vertical

Poner mismo padding arriba y abajo al elemento padre.

Y elementos en linea.

###  🚩 <b>Posicionamiento</b>

#### 🏮Static

Es el valor por defecto

El elemento sigue el flujo correspondiente.

Aunque se use top,bottom,left,right, o z-index NO las aplica

#### 🏮Relative

Como static pero SÍ atiende top, bottom, left, right, o z index a partir de la posición que le corresponde por el flujo

#### 🏮Fixed

Se le aplica top,bottom,left,right o z index en relacion al documento.

No atiende al scroll.

Permanece en el mismo sitio siempre.

#### 🏮Absolute

Se comporta como fixed pero en relación a la primera etiqueta antecesora que tenga position:relative

#### 🏮Sticky

Relative hasta llegar a una posición de scroll y a partir de una entonces fixed
