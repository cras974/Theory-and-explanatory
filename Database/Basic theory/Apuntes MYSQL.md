# 💠  Apuntes MYSQL

---

## ⚫  COMANDOS MYSQL
---

### 🔐 Objeto base de datos

<br>

<b>Crea una tabla si no existe y le pone un nombre</b>
```SQL
    CREATE DATABASE IF NOT EXISTS EJEMPLO;
```
<b>Usa la base de datos llamada ejemplo</b>
```SQL
    USE EJEMPLO;
```
<b>Cambia los caracteres de la base de datos a utf8</b>
```SQL
    ALTER DATABASE EJEMPLO CHARACTER SET utf8;
```
<b>Borra la base de datos ejemplo</b>
```SQL
    DROP DATABASE EJEMPLO;
```
---

### 🌑 Objeto de tablas

<b>Crear tablas, ponemos create y luego cada columna </b>
```SQL
    CREATE TABLE EJEMPLO (
    id int,
    nombre varchar(45)
    );
```
<b> Cambiar la tabla y modificarla, añadir una columna o eliminarla. </b>
```SQL
    ALTER TABLE EJEMPLO
    ADD COLUMN apellidos varchar(80);

    ALTER TABLE EJEMPLO
    DROP COLUMN apellidos;
```

<b> Eliminar la tabla </b>

```SQL
    DROP TABLE EJEMPLO;
```
---

### <b> 🌘 Objeto Indice </b>
```SQL

    Se considera indices, PRIMARY KEY, FULLTEXT
    FOREIGN KEY, UNIQUE.

    ALTER TABLE ADD [tipo_indice] INDEX nombre_indice (campo);

    ALTER TABLE ejemplo / CREATE TABLE ejemplo
    ADD INDEX idx_nombre (nombrejemplo),
    ADD INDEX idx_nombre (apellidos,nombre),
    ADD UNIQUE INDEX idx_mombre (DNI),
    Si queremos que coga x letras al ordenar.
    ADD INDEX idx_nombre (nombre(4),edad)

    (Para crear un indice fuera de un alter)
    CREATE INDEX idx_nombre ON nom_tabla(campo)
    CREATE FULLTEXT idx_nombre ON nom_tabla(campo,campo2)
```

---

###  🔔  Definicion de datos

<b> Hacer que un dato sea obligatorio </b>
```SQL
    col_name col_definition NOT NULL 
```

<b> Hacer que sea un dato unico </b>
```SQL
    col_name col_definition UNIQUE
```

<b> Hacer que el dato se auto incremente </b>
```SQL
    col_name col_definition AUTO_INCREMENT

    Si queremos que empiece desde cierto numero.

    AUTO_INCREMENT = 100
```

<b> Hacer que un dato sea clave primaria </b>
```SQL
    col_name col_definition PRIMARY KEY
```

<b> Hacer que la clave primaria sean varios campos </b>
```SQL
    PRIMARY KEY(ID,NOMBRE)
```

// 🚩 Las claves primarias siempre deben llevar NOT NULL y UNIQUE y       posiblemente AUTO_INCREMENT //

<b> Chequear que los datos sean algo especifico </b>
```SQL
    EDAD tinyint,
    CHECK (EDAD>=18)
```

<b> Para darle un nombre a una clave </b>
```SQL
    CONSTRAINT pk_ejemplo PRIMARY KEY(ID)
                /NOMBRE/

    CONSTRAINT fk_ej_ej2 FOREING KEY (id_ejemplo2) REFERENCES EJEMPLO2(id)
                /NOMBRE/
    
    /* Para eliminar el chequeo de FK, set foreing_key_checks=0; */
```

<b> Definir una clave ajena, ponemos la tabla de la que viene y el campo. </b>

```SQL
    FOREIGN KEY id_ejemplo2 REFERENCES ejemplo2(id)
                 /NOMBRE/
```

<b> Definicion de clave ajena completa </b>

```SQL
    CONSTRAINT fk_ej_ej2 FOREIGN KEY (id_ejemplo2) REFERENCES EJEMPLO2(id) on update cascade on delete restrict
```

<b> Alterar y modificar tablas <b>
```SQL
    ALTER TABLE nombre_tabla
    INSTRUCCION

        /Estas son algunas opciones/

        ADD nombre_col definicion 
        (Añada una columna y el tipo de dato)
        /Se puede hacer con claves e indices/

        CHANGE col_original nombre_nuevo VARCHAR(30) ...
        /Cambia el nombre y todo lo definido/

        DROP nombre_col;
        /Sirve para borrar desde columnas hasta keys e indices/

        ADD PRIMARY KEY(nombrekey)

        DROP DEFAULT

        RENAME col_antiguo TO nombre_nuevo
        /Tambien pueden ser keys,indices o tablas./
        
        ALTER columna SET DEFAULT 'valor' | DROP DEFAULT

        MODIFY column tipo_datos opciones ...

        LOCK = DEFAULT|NONE|SHARED|EXCLUSIVE
        SHARED = Permite el uso de la tabla
        EXCLUSIVE = No permite nada mientras estes editando
        DEFAULT = Permite ver pero no editar
        NONE = No tiene
        (Esto hace que bloquee la tabla para que no entren mientras yo haga modificaciones en la tabla.)

```
---

<h2>⚠️ Insercion y modificación de datos </h2>

<b> Insercion de datos </b>

```SQL
-- SI NO PERMITE USAR COMANDOS PELIGROSOS--

SET SQL_SAFE_UPDATES =0;

----

INSERT INTO `nom_tabla` (`colum1`,`column2`,`column3`)
    (dato1,dato2,dato3),
    (dato1,dato2,dato3);

--Se podria poner default o null en vez de un dato.--

INSERT INTO `departamentos` (`dep_no`,`dnombre`,`localidad`) VALUES 
    (10,'CONTABILIDAD','BARCELONA'),
    (20,'INVESTIGACION','VALENCIA'),
    (30,'VENTAS','MADRID'),
    (40,'PRODUCCION','SEVILLA');

Insertar datos de una tabla a otra.

SELECT * FROM bd.tabla;
CREATE TABLE nom_tabla LIKE bd.tabla;
--La tabla se creará en la BD que estamos usando.--

--Añadir los datos de los empleados del tabla1 a nuestra tabla tabla2 --

INSERT INTO nom_tabla --La que quieres insertar--

SELECT * FROM bd.tabla WHERE colum=condicion;

--Para datos especificos--

INSERT INTO nom_tabla (column1,column2,column3)
SELECT column1,column2,column3 FROM bd.tabla 
HERE column=condicion;

--Podemos poner un dato concreto en el select para que se cambie--

--Para extraer solo un dato en concreto--

INSERT INTO nom_tabla VALUES
--Debemos ir poniendo los datos de uno en uno--
('dato1','dato2','dato3','dato4',NULL,DEFAULT,
(SELECT nom_column
FROM nom_tabla
WHERE column='condicion'));

# O si tiene varios valores

INSERT INTO ARTICULOS
SELECT 'dato1', VALOR_SELECT,'dato2','dato3'
FROM TABLA
WHERE column='condicion'

--Ponemos el select para extraer el dato que queremos, el SELECT, solo devuelve un valor.--

```

<b> SELECT </b>

```SQL
--Deberiamos estar en la bd que queremos usar.--

SELECT *
FROM TABLA;
--Imprime todos los campos--

SELECT column1,column2
FROM TABLA
WHERE column="dato";

SELECT APELLIDO,OFICIO
FROM EMPLEADOS
WHERE OFICIO='VENDEDOR';

SELECT APELLIDO,OFICIO
FROM EMPLEADOS
WHERE OFICIO='VENDEDOR' AND SALARIO>=25000;
--Para poner dos condiciones se pueden poner and u or.--
/And es excluyente, or no./

SELECT APELLIDO,OFICIO
FROM EMPLEADOS
WHERE SALARIO>=25000 AND NOT(OFICIO='VENDEDOR');
                            OFICIO!='VENDEDOR';
--Para negar algo--

SELECT APELLIDO,SALARIO,OFICIO,DEP_NO
FROM empleados JOIN DEPARTAMENTOS
WHERE SALARIO>2500 AND NOT(OFICIO='VENDEDOR') OR DNOMBRE='INVESTIGACIÓN';
--Podemos usar dos tablas con JOIN, y poner uno u otro nombre en los campos.--

```

<b> UPDATE </b>

```SQL

UPDATE nom_tabla
SET nom_column=valor;

UPDATE EMPLEADOS
SET COMISION=100;

--Hace que comision en empleados sean 100.--

UPDATE EMPLEADOS
SET COMISION=100
WHERE COMISION IS NULL;
--Cambia los valores de comision que estén vacios.--

```

<b> Eliminar datos </b>

```SQL

FILAS COMPLETAS

DELETE FROM nom_column
WHERE condicional;

DELETE FROM EMPLEADOS
WHERE COMISION IS NULL;
--Elimina las filas con comision vacio.--

DATOS CONCRETOS

UPDATE EMPLEADOS
SET OFICIO=''
WHERE EMP_NO=7643;

UPDATE EMPLEADOS
SET OFICIO=NULL
WHERE EMP_NO=7499;
```
---

### ⚠️ Tipos de datos

<b>  Datos numericos </b>

    bit (Acepta 0 o 1, verdadero, falso)

    Tinyiny (1 Byte)

    SmallInt (2 Bytes)

    MediumInt (3 Bytes)
    
    INT (4 Bytes)

    BIGINT (8 Bytes)
    
    Float (Para tener decimales y numeros muy precisos.)

    XReal (Numero con precision y algunos decimales.)

    🚩// Se les puede poner detras UNSIGNED para 
    marcar que no queremos numeros negativos//

<b> Ⓜ️ Datos de caracter </b>

    Char (Hasta 255 caracteres)
    Varchar (Recomendable, caracteres promedio)
    text (Mas texto)
    Mediumtext (Texto grande)
    Longtext (Textos gigantes)

<b> 🕚 Fecha y hora </b>

    Date (Indica una fecha)
    Time (Es para la hora)
    DateTime (Fecha y hora)
    TimeStamp[(M)] (Toma la fecha actual)
    Year (2 o 4) Para el año en 2 o 4 digitos

<b> 🅿️ Enumerados y connjuntos </b>

    ENUM('valor1','valor2') Funciona como listas

---

## ♨️ Motores BD

<b> Motores de base de datos </b>

    InnoDB Es el que permite foreing key

<b> Poner el motor en el codigo //Va dentro del codigo de la tabla//</b>

    ENGINE = nombre_motor

---

### 💯 Ejemplo de script

<center><b> 1️⃣  EJEMPLO</b>

```SQL
    CREATE DATABASE IF NOT EXISTS EJEMPLO;
    USE EJEMPLO;

    create table if not exists ejemplo2(
    id int
    );

    create table if not exists ejemplo(
    id int AUTO_INCREMENT NOT NULL UNIQUE,
    nombre varchar(45) NOT NULL,
    EDAD tinyint,
    id_ejemplo2 int,
    CONSTRAINT pk_ejemplo PRIMARY KEY(ID),
    foreign key id_ejemplo2 REFERENCES ejemplo2(id),
    CONSTRAINT fk_ej_ej2 FOREING KEY (id_ejemplo2) REFERENCES EJEMPLO2(id)
    );
```
