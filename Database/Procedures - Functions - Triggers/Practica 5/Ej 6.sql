DROP PROCEDURE IF EXISTS notas;

DELIMITER //

CREATE PROCEDURE notas(IN n_dni VARCHAR(50), OUT aprobadas INT, OUT suspensas INT)
BEGIN
    DECLARE existe INT DEFAULT 0;

    SET aprobadas = 0;
    SET suspensas = 0;

    SELECT COUNT(*) INTO existe FROM alumnos WHERE dni = n_dni;

    IF existe > 0 THEN
        SELECT COUNT(*) INTO aprobadas FROM notas_alumnos 
        WHERE dni = n_dni AND nota >= 5;

        SELECT COUNT(*) INTO suspensas FROM notas_alumnos 
        WHERE dni = n_dni AND nota < 5;
    END IF;

END //

DELIMITER ;