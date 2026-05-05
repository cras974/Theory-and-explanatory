DROP PROCEDURE IF EXISTS MostrarsodaelpmE;

DELIMITER //

CREATE PROCEDURE MostrarsodaelpmE(p_nombre_rev VARCHAR(50))
BEGIN
    -- 1. PRIMERO todas las variables
    DECLARE v_nombre VARCHAR(50);
    DECLARE fin INT DEFAULT 0;
    DECLARE v_real VARCHAR(50);

    DECLARE cur CURSOR FOR 
        SELECT apellido FROM empleados 
        JOIN departamentos USING (dep_no)
        WHERE dnombre = REVERSE(p_nombre_rev);

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

    OPEN cur;
    FETCH cur INTO v_nombre;

    WHILE fin = 0 DO
        SELECT v_nombre;
        FETCH cur INTO v_nombre;
    END WHILE;

    CLOSE cur;
END //

DELIMITER ;