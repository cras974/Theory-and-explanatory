DELIMITER //

/*8.   Escribe un procedimiento que reciba un número real de entrada, que representa el valor de la nota de un alumno, 
y muestre un mensaje indicando qué nota ha obtenido teniendo en cuenta las siguientes condiciones:*/

DROP PROCEDURE IF EXISTS comprobar_nota//
CREATE PROCEDURE comprobar_nota (IN nota decimal(2,1), OUT calificacion varchar(50))

BEGIN
	CASE
		WHEN nota >= 0 and nota < 5 then SET calificacion = "Insuficiente";
        WHEN nota >= 5 and nota < 6 then set calificacion = "Aprobado";
        WHEN nota >= 6 and nota < 7 then set calificacion = "Bien";
        WHEN nota >= 7 and nota < 9 then set calificacion = "Notable";
        WHEN nota >= 9 and nota <= 10 then set calificacion = "Sobresaliente";
        ELSE SET calificacion = "Nota no valida";
	end case;
END //

delimiter ;

CALL comprobar_nota((6),@calificacion);
SELECT @calificacion;