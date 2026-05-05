DROP TRIGGER IF EXISTS añadir_persona;


DELIMITER //

CREATE TRIGGER añadir_persona
AFTER INSERT ON persona
FOR EACH ROW
BEGIN

	INSERT INTO nuevosdatos(codigo,cuando,tipo) 
    VALUES (new.codigo,now(),"i");

END //

DELIMITER ;

INSERT INTO persona VALUES (1,"pepe",20)