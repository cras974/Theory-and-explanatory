DELIMITER //

CREATE PROCEDURE actualizar_columna_edad ()
BEGIN
    UPDATE alumnos 
    SET edad = calcular_años(fecha_nacimiento);
END //

DELIMITER ;

CALL actualizar_columna_edad();

SELECT * FROM alumnos;