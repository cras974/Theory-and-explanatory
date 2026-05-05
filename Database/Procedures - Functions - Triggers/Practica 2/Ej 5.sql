/*Realiza un procedimiento MostrarAbreviaturas que muestre las tres primeras letras del nombre de cada empleado.*/

DROP PROCEDURE IF EXISTS MostrarAbreviaturas;

DELIMITER //

CREATE PROCEDURE MostrarAbreviaturas()

BEGIN

	DECLARE v_nombre varchar(50);
    
    DECLARE fin_cursor BOOLEAN default false;
    
    DECLARE cursor_empleados CURSOR FOR
		SELECT apellido FROM empleados;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin_cursor = true;
    
    OPEN cursor_empleados;
    
    FETCH cursor_empleados INTO v_nombre;
    
    WHILE fin_cursor = false DO
    
		SELECT left (v_nombre, 3) AS Abreviatura;
        
        FETCH cursor_empleados INTO v_nombre;
        
	END WHILE;
    
    CLOSE cursor_empleados;

END //

DELIMITER ;

call empleados.MostrarAbreviaturas();