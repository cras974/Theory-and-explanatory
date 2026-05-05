DROP FUNCTION IF EXISTS semana;
DELIMITER //
CREATE FUNCTION semana (n_dia int)
RETURNS varchar(30)
DETERMINISTIC

BEGIN

	DECLARE dia varchar(30);
    
    SET dia = CASE
		WHEN n_dia = 1 then "Lunes"
        WHEN n_dia = 2 then "Martes"
        WHEN n_dia = 3 then "Miercoles"
        WHEN n_dia = 4 then  "Jueves"
        WHEN n_dia = 5 then "Viernes"
        WHEN n_dia = 6 then "Sabado"
        WHEN n_dia = 7 then "Domingo"
        ELSE "Opcion no valida"
        END;
	RETURN dia;

END //
DELIMITER ;

select procedimientos.semana(3) AS "Dia de la semana";