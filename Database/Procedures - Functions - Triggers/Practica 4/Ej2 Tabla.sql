CREATE TABLE log_cambios_email(
id int primary key,
id_alumno int,
fecha_hora date,
old_email varchar(50),
new_email varchar(50)
)