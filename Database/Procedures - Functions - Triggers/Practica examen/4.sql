use empleados;
CREATE TABLE if not exists EQUIPOS (
 CodEquipo VARCHAR(4) PRIMARY KEY,
 Nombre VARCHAR(30) NOT NULL,
 Localidad VARCHAR(15)
);
 
 drop function if exists equipo_nombre;
 delimiter //
 create function equipo_nombre (f_CodEquipo varchar(4))
 returns varchar(100)
 deterministic
 begin
 
 declare nombre_equipo varchar(30);

 declare exit handler for not found 
 return "No existe el id del equipo introducido" ;
 
 select nombre into nombre_equipo from equipos where CodEquipo = f_CodEquipo;
 
 return nombre_equipo;
 
 end //
 delimiter ;
 select equipo_nombre(1);