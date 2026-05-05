
USE test;

DROP TRIGGER IF EXISTS crear_email_before_insert;

DELIMITER //

CREATE TRIGGER crear_email_before_insert
before insert on alumnos
for each row
BEGIN

	declare v_email varchar(250);
    if new.email is null then 
		call crear_email(new.nombre,new.ape1,new.ape2,'g.educaand.es',v_email);
        set new.email = v_email;
    end if;
    
END //

delimiter ;


