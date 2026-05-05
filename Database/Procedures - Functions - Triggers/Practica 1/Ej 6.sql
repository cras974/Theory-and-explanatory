DROP PROCEDURE IF EXISTS insertar_alumno;
DELIMITER //
CREATE PROCEDURE insertar_alumno(in id int unsigned, in nombre varchar(50), in apellido1 varchar(50), in apellido2 varchar(50), out p_error int)
BEGIN

	DECLARE CONTINUE HANDLER FOR 1062
    BEGIN
		SET p_error = 1;
	END;
    
    SET p_error=0;
        
	INSERT INTO alumno VALUES (id,nombre,apellido1,apellido2);

END //

DELIMITER ;

call test.insertar_alumno(1, 'miguel', 'garcia', 'cortes', @p_error);
select @p_error;

SELECT * FROM test.alumno;