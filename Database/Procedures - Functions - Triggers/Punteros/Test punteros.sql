CREATE DATABASE IF NOT EXISTS TEST;
USE TEST;
CREATE TABLE alumnos(
  id int unsigned auto_increment primary key,
  nombre varchar(50),
  ape1 varchar(50),
  ape2 varchar(50)
);

insert into test.alumnos (nombre, ape1, ape2) values
('Miguel','Garcia','Cortes'),
('Pepe','Gonzalez','Perez'),
('Maria','Rodriguez','Lopez');

ALTER TABLE alumnos
ADD column email varchar(20);

------------

delimiter //

drop procedure if exists iniciales//
create procedure iniciales(IN nom varchar(20), in ap1 varchar(20), in ap2 varchar(20), out mensaje varchar(20) )
begin

	declare nombre varchar(20);
    declare ape1 varchar(20);
    declare ape2 varchar(20);
    declare email varchar(20);
    
    set nombre= lower(left(nom,1));
    set ape1= lower(left(ap1,1));
    set ape2= lower(left(ap2,1));
    
	SET MENSAJE = concat(nombre,ape1,ape2,'@',email);
	

end //