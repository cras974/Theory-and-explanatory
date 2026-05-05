DROP FUNCTION IF EXISTS Transcurso;
DELIMITER //

CREATE FUNCTION Transcurso (fecha1 DATE, fecha2 DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE diferencia INT;

    IF fecha1 >= fecha2 THEN
        SET diferencia = DATEDIFF(fecha1, fecha2);
    ELSE
    
        SET diferencia = DATEDIFF(fecha2, fecha1);
    END IF;

    RETURN diferencia / 365;
END //

DELIMITER ;

select procedimientos.Transcurso('2010-02-01', '2020-02-01');
