/*5.   Dada la siguiente tabla persona (peso, estado) Realizar un procedimiento para determinar si la persona puede donar sangre: 
si el peso es menor a 50 guarde en estado “no admitido”, en caso contrario sería “admitido”.*/

CREATE TABLE IF NOT EXISTS persona(
peso int,
estado varchar(100));

DROP PROCEDURE IF EXISTS donador;

DELIMITER //

CREATE PROCEDURE donador(IN p_peso int)

BEGIN 
	
    DECLARE n_estado varchar(200);
    
	IF p_peso > 50 then 
		SET n_estado = "Admitido";
	
    ELSEIF p_peso < 50 then
		SET n_estado = "No admitido";
	
    END IF;
    
    INSERT INTO persona (peso,estado) VALUES (p_peso, n_estado);

END //

DELIMITER ;