# 💠  Apuntes MYSQL subconsultas

---

## ⚫  CONSULTAS SQL AVANZADO

#### Guia

    [Opcional]
    |Opcional dentro de opcional| / o
    col1,col2 = Columnas
    dato1,dato2 = Datos

#### ⚠️ CONDICIONALES

```SQL

SELECT col1,col2

[ALL | DISTINCT]

--ALL = Por defecto, todos los valores--

--DISTINCT = Solo los valores distintos--

FROM TABLA_OBJETIVO

--Condiciones o-- [Puede haber varios]

WHERE  <- Tema anterior 

GROUP BY col1

    /*El select debe tener los campos y agrupara
     por ese campo, deberia estar acompañado de
     alguna funcion*/

     SELECT col1
     FROM tabla1
     GROUP BY col1

     #Si queremos actuar sobre la cantidad reflejada

     SELECT col1
     FROM tabla1
     GROUP BY col1
     HAVING count(col1)>numero

     #Puede, o puede no tener HAVING

HAVING col1 condicional (Como where)

    /* Funciona como un where, pero actua sobre las otras funciones y condicionales, la 
    diferencias es que el where actua sobre la tabla como tal, el having sobre el resultado */

    #Por lo general se usará con un GROUP BY.

ORDER BY [col_opcional |DESC/ASC|],col1 ASC/DESC;

    #ASC Es de menor a mayor
    #DESC Es de mayor a menor
    #La columna opcional hace que se ordenen agrupados en la otra columna

    SELECT * FROM empleados.empleados
    ORDER BY 8,2 ASC
    #La columna puede ser un numero, esto indica su posicion en el select

LIMIT numero

    #Seleciona las filas indicadas

    LIMIT x,y

    #Salta a la fila x y coge las indicadas
```

#### ⚠️ FUNCIONES

| Nombre | Descripción |
| :--- | :--- |
| **AVG(expr)** | Devuelve el valor medio de `expr` |
| **COUNT(expr)** | Devuelve un contador con el número de valores distintos de NULL en las filas recuperadas por una sentencia SELECT |
| **MIN(expr)**<br>**MAX(expr)** | Devuelve el valor mínimo o máximo de `expr`. **MIN()** y **MAX()** pueden tomar como argumento una cadena, en ese caso devolverán el valor de la cadena mínima o máxima. |
| **STD(expr)**<br>**STDDEV(expr)** | Devuelve la desviación estándar de la expresión |
| **SUM(expr)** | Devuelve la suma de la expresión `expr`. Si el conjunto de resultados no tiene filas, devuelve NULL. |

##### Ejemplos de uso

```SQL
SELECT col1, col2
FROM tabla
ORDER BY col1
LIMIT 1;

-- De manera menos eficiente abajo --

SELECT col1,col2
FROM tabla
WHERE col1=(select min(col1) FROM tabla);


--Uso completo--

SELECT col1, SUM(col2)
FROM tabla
WHERE col1 IS NOT NULL
GROUP BY col1
HAVING SUM(COL1) condicion;

--Operadores--

SELECT max(salario) as SM, min(salario) as SB, SM-SB 
FROM empleados

#Puede que los alias no funcionen


```

### 📊 Ejemplos Prácticos de Funciones SQL

 **`Productos`**:

| ID | Nombre | Precio | Notas |
| :---: | :--- | :---: | :--- |
| **1** | Teclado | `20` | |
| **2** | Ratón | `10` | |
| **3** | Monitor | `100` | |
| **4** | USB | `10` | |
| **5** | Manual | `NULL` | *Sin precio* |

---

```SQL

1. AVG (Promedio)
Calcula la media aritmética de una columna numérica.

SELECT AVG(Precio) FROM Productos;
Resultado: 35

📝 Cálculo: (20 + 10 + 100 + 10) / 4 
Nota: Se ignora la fila con valor NULL.

2. COUNT (Contar)
Cuenta el número de filas con datos (no nulos).

SQL

SELECT COUNT(Precio) FROM Productos;
Resultado: 4

📝 Explicación: Solo hay 4 productos con precio. El "Manual" no se cuenta porque su precio es NULL.

3. MIN y MAX (Mínimos y Máximos)
Encuentra los valores extremos (números o alfabéticos).

Con Números:

SQL

SELECT MIN(Precio), MAX(Precio) FROM Productos;
Resultado: Mínimo: 10 | Máximo: 100

Con Texto:

SQL

SELECT MIN(Nombre), MAX(Nombre) FROM Productos;
Resultado:

Mínimo: Manual (Orden alfabético: M antes que R, T, U...)

Máximo: USB (Orden alfabético: U es la última)

4. SUM (Suma Total)
Suma todos los valores de la columna.

SQL

SELECT SUM(Precio) FROM Productos;
Resultado: 140

📝 Cálculo: 20 + 10 + 100 + 10

5. STD (Desviación Estándar)
Mide la dispersión de los datos (qué tan alejados están los precios del promedio).

SQL

SELECT STD(Precio) FROM Productos;
Resultado: 37.74

📝 Explicación: Indica que hay mucha diferencia de precios (ej. 10 vs 100).


# Si tenemos en un operador con un where como > o <, debemos poner si devuelve mas de una linea:

# ANY Para que devuelva alguna

# ALL Para que devuelva todas

```
##### 🚩Si la operacion da null por otros null

```SQL

SELECT col1, col2 + IFNULL(colnula 0)

#IFNULL Hará que el valor nulo se cambie por 0

```

##### 🚩Crear un alias

```SQL

SELECT col1, funcion(col2) AS 'ALIAS'
FROM nom_tabla AS 'ALIAS'

#Se le asignara el nombre del alias

#Si cambiamos la tabla, se referenciará siempre con el alias a partir de ese momento

#Se puede obviar el AS

```

##### 🚩 Valor distinto no repetido

```SQL

SELECT DISTINCT col1

#Hace que los valores no se repitan.

#Se puede usar con las funciones.

SELECT COUNT(DISTINCT col1)

```

#### ⚠️ INNER JOIN

```SQL

USO DEL ON

    SELECT *
    FROM EMPLEADOS e JOIN DEPARTAMENTOS d ON e.dep_no=d.dep_no;

    --Despues del from [tabla] ponemos un alias para abreviar, en este caso e y d--

    --Unimos las tablas por su clave en comunm en este caso dep_no--

    --Le decimos a mysql que un dep_no es de una tabla y otro de la otra pero son =--

USO DEL USING

    SELECT*
    FROM EMPLEADOS JOIN DEPARTAMENTOS USING (dep_no);

    --Se usa using cuando el nombre del campo es igual--
    --Es mas simple que el ON--

Debemos tener en cuenta que el using es mas simple, pero lo usaremos unicamente cuando el campo sea igual en las tablas.

Si es distinto usaremos ON, especificando los campos.

Se pueden concatenar varios JOIN para unir mas de 2 tablas.

    SELECT*
    FROM ALUMNOS A JOIN NOTAS N ON A.DNI=N.DNI JOIN ASIGNATURAS AG ON AG.COD=N.COD

    --Se unirian las 3 tablas--

USO DEL CROSS JOIN

    SELECT *
    FROM EMPLEADOS JOIN DEPARTAMENTOS;

    --Mezcla todos los datos entre si--
    --Rara vez usado--

```

#### ⚠️ LEFT Y RIGHT JOIN

```SQL

USO DEL RIGHT JOIN

    FROM EMPLEADOS E RIGHT JOIN DEPARTAMENTOS D ON E.DEP_NO=D.DEP_NO

    /*Right indica que todos los datos de la tabla a la derecha del join se mostraran aunque no tenga mas datos 
    asignados, en este caso departamentos*/

    FROM EMPLEADOS E LEFT JOIN DEPARTAMENTOS D ON E.DEP_NO=D.DEP_NO

    --Left indica lo mismo que right pero al contrario--

A diferencia de los INNER JOIN, que muestra solo los datos que esten en las 2 tablas.

Esta JOIN indica la tabla completa de la izquierda o derecha, juntando los datos que coinciden con los no indicados.

Este JOIN tambien se usa con USING u ON
```

#### ⚠️ SUBCONSULTA DE FROM

```SQL

--Se pueden usar subconsultas en un from, por ejemplo para agrupar consultas.

#2. Número del departamento con el mayor número de empleados (igual que el anterior , pero sacando el número

SELECT DNOMBRE, TOTAL
FROM (SELECT DEP_NO, COUNT(EMP_NO) AS TOTAL FROM EMPLEADOS GROUP BY DEP_NO) AS T1
		JOIN DEPARTAMENTOS ON departamentos.DEP_NO=t1.DEP_NO
ORDER BY 2 DESC
LIMIT 1;

--Esto nos permite poner, por ejemplo un max de un count, que de normal, no dejaria.

```