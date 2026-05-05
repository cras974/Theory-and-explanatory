# 📑 APUNTES XPATH

### 🛠️ Tabla de Expresiones y Resultados

| Expresión | Resultado / Descripción |
| :--- | :--- |
| `*` | **Comodín:** Selecciona todos los elementos en el nivel actual. |
| `/` | **Raíz o Nivel:** Al inicio indica la raíz; en medio baja un nivel jerárquico directo. |
| `//` | **Búsqueda global:** Selecciona nodos en cualquier lugar del documento. |
| `/obras` | Selecciona el nodo raíz `obras` y todos sus descendientes. |
| `//obras` | Todos los nodos `obras` del documento, sin importar su ubicación. |
| `/obra` | **Vacío:** Los nodos `obra` no están en la raíz (normalmente están dentro de `obras`). |
| `/obras/museo` | **Vacío:** Si `museo` no es un hijo directo de `obras`, no lo encontrará. |
| `/obras//museo` | Todos los nodos `museo` que dependan (directa o indirectamente) de `obras`. |
| `/obras/obra/*` | Todos los nodos hijos que dependen directamente de los nodos `obra`. |

---

### 🔍 Notas de Análisis

* **Jerarquía Estricta:** El uso de `/` requiere que el elemento esté exactamente en ese nivel. Si el nodo está anidado más profundo, la consulta devolverá un resultado vacío.

### Tabla de Expresiones con Atributos

Expresiones     Resultado

//@*            Todos los atributos de todos los nodos

//obra/@*       Todos los atributos de todos los nodos obra

//obra/@pais    El atributo pais del nodo obra

//obra[@pais="Francia"]

//museo[@visible="true"]/../titulo/string()  Devuelve los caracteres volviendo atras con ..

### Funciones XPATH que manejan cadenas de caracteres

Expresiones                 Resultado

//obra/titulo/string()      Todos los titulos de las obras (Solo el texto por string)

//obra/@pais/string()       Todos los valores (Solo el texto) de los atributos pais de los nodos obra

//obra/@pais/text()         En resultado vacio. La funcion text() no tiene efecto sobre los atributos

//titulo[starts-with(text(),"L")]   Todos los titulos de las obras que comienzan por L MAYUSCULA

//titulo[contains(text(),"h")]      Todos los titulos de las obras que contienen una h MINUSCULA

//obra[starts-with(text(),"l") or starts-with(text(),"L")]

Se compara con alguna de las dos L o l

//titulo[starts-with(lower-case(text()),"l")]   

El titulo ahora se compara con minuscula, sin importar lo que haya debido al lower-case que precede al text

//obra/@pais/upper-case(string())    Todos los paises de las obras en mayusculas