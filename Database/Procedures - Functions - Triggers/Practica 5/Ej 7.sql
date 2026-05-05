DROP PROCEDURE IF EXISTS EstadisticasModulo;

DELIMITER //

CREATE PROCEDURE EstadisticasModulo(p_nombre_modulo VARCHAR(100))
BEGIN

    DECLARE v_nombre VARCHAR(100);
    DECLARE v_nota FLOAT;
    DECLARE fin INT DEFAULT 0;
    

    DECLARE c_sus, c_apr, c_not, c_sob INT DEFAULT 0;
    DECLARE max_nota FLOAT DEFAULT -1;
    DECLARE min_nota FLOAT DEFAULT 11;
    DECLARE max_alumn, min_alumn VARCHAR(500) DEFAULT '';
    DECLARE v_existe INT DEFAULT 0;


    DECLARE cur CURSOR FOR 
        SELECT a.nombre, n.nota 
        FROM alumnos a 
        JOIN notas_alumnos n ON a.dni = n.dni 
        JOIN modulos m ON n.id_modulo = m.id_modulo
        WHERE m.nombre = p_nombre_modulo;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;


    SELECT COUNT(*) INTO v_existe FROM modulos WHERE nombre = p_nombre_modulo;
    
    IF v_existe = 0 THEN
        SELECT 'El módulo no existe' AS Error;
    ELSE
        OPEN cur;
        FETCH cur INTO v_nombre, v_nota;

        IF fin = 1 THEN
            SELECT 'El módulo no tiene alumnos o datos' AS Error;
        ELSE
            WHILE fin = 0 DO
                SELECT v_nombre AS Alumno, v_nota AS Nota;

                IF v_nota < 5 THEN SET c_sus = c_sus + 1;
                ELSEIF v_nota < 7 THEN SET c_apr = c_apr + 1;
                ELSEIF v_nota < 9 THEN SET c_not = c_not + 1;
                ELSE SET c_sob = c_sob + 1;
                END IF;

                IF v_nota > max_nota THEN
                    SET max_nota = v_nota;
                    SET max_alumn = v_nombre;
                ELSEIF v_nota = max_nota THEN
                    SET max_alumn = CONCAT(max_alumn, ', ', v_nombre);
                END IF;

                IF v_nota < min_nota THEN
                    SET min_nota = v_nota;
                    SET min_alumn = v_nombre;
                ELSEIF v_nota = min_nota THEN
                    SET min_alumn = CONCAT(min_alumn, ', ', v_nombre);
                END IF;

                FETCH cur INTO v_nombre, v_nota;
            END WHILE;

            SELECT c_sus AS Suspensos, c_apr AS Aprobados, c_not AS Notables, c_sob AS Sobresalientes;
            SELECT max_alumn AS 'Alumno(s) Nota Max', max_nota AS 'Nota Max';
            SELECT min_alumn AS 'Alumno(s) Nota Min', min_nota AS 'Nota Min';
        END IF;
        CLOSE cur;
    END IF;
END //

DELIMITER ;