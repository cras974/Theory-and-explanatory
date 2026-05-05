# :warning: XML



###  🚩 <b>Entidades en los DTD</b>

```XML

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <!DOCTYPE fichas[
        <!ENTITY poblacion "Atarfe">
    ]>

<fichas>
    <ficha>
        <empresa nombre="Tejidos remolino"/>
        <direccion> &poblacion </direccion>
    </ficha>
    <ficha>
        <empresa nombre="Pepe motors"/>
        <direccion> &poblacion </direccion>
    </ficha>
</fichas>

```

```XML

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <!DOCTYPE cv[
        <!ELEMENT cv(nombre,direccion,telefono,fax?,email+,idiomas)>    #Declara los campos, si tiene ? es opcional, si tiene +, uno o mas
        <!ELEMENT nombre (#PCDATA)>                                     #Cadena de texto
        <!ELEMENT telefono (#PCDATA)>
        <!ELEMENT direccion (#PCDATA)>
        <!ELEMENT fax (#PCDATA)>
        <!ELEMENT email (#PCDATA)>
        <!ELEMENT idiomas (idioma*)>                                    #Requiere que tenga un elemento idioma dentro
        <!ELEMENT idioma (#PCDATA)>
    ]>

<cv>
    <nombre> Miguel Ángel </nombre>
    <direccion> C/Cervantes </direccion>
    <telefono> 698 34 21 09 </telefono>
    <email> ejemplo@email.com </email>
    <email> ejemplo2@email.com </email>
    <idiomas>
        <idioma> Inglés </idioma>
        <idioma> Francés </idioma>
        <idioma> Italiano </idioma>
    </idiomas>
</cv>


```