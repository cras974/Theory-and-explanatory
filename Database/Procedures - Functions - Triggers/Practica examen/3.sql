USE EMPLEADOS;
DROP TRIGGER IF EXISTS Modificar_before_insert_id;
create table if not exists altas (id int, nombre varchar(30));
DELIMITER //

CREATE TRIGGER Modificar_before_insert_id
BEFORE insert ON altas
FOR EACH ROW
BEGIN
    declare id_aumentado int;
    set id_aumentado = (select id from altas order by 1 desc limit 1);
    
    set new.id = id_aumentado + 1;
END//

DELIMITER ;

insert into altas
values (5,'Miguel');

select * from altas;


