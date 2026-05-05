#ALTER TABLE alumno ADD COLUMN email VARCHAR(100);
DROP PROCEDURE IF EXISTS crear_email;
DELIMITER //

CREATE PROCEDURE crear_email (
    IN p_nombre VARCHAR(50),
    IN p_apellido1 VARCHAR(50),
    IN p_apellido2 VARCHAR(50),
    IN p_dominio VARCHAR(50),
    OUT p_email VARCHAR(100)
)
BEGIN
    SET p_email = LOWER(CONCAT(
        LEFT(p_nombre, 1),
        LEFT(p_apellido1, 3),
        LEFT(p_apellido2, 3),
        '@',
        p_dominio
    ));
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE actualizar_columna_email (IN p_dominio VARCHAR(50))
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_nom, v_ape1, v_ape2, v_email_generado VARCHAR(50);
    
    DECLARE cur1 CURSOR FOR SELECT id, nombre, apellido1, apellido2 FROM alumno;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur1;

    read_loop: LOOP
        FETCH cur1 INTO v_id, v_nom, v_ape1, v_ape2;
        IF done THEN
            LEAVE read_loop;
        END IF;

        CALL crear_email(v_nom, v_ape1, v_ape2, p_dominio, v_email_generado);

        UPDATE alumno SET email = v_email_generado WHERE id = v_id;
    END LOOP;

    CLOSE cur1;
END //

DELIMITER ;



INSERT INTO alumno (id, nombre, ape1, ape2) VALUES (1, 'Juan', 'Perez', 'Garcia');

CALL actualizar_columna_email('iescuravalera.es');

SELECT * FROM alumno;
