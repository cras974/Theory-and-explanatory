DELIMITER //

#Calcula salario maximo, minimo y medio

CREATE PROCEDURE calculos_salarios (IN  p_dpto varchar(50) , OUT s_max INT, OUT s_min INT, OUT s_avg INT)

BEGIN

DECLARE dep_numero INT;

SET dep_numero = (SELECT dep_no
				FROM departamentos
				WHERE dnombre=p_dpto);
                
SELECT max(salario), min(salario), avg(salario) INTO s_max, s_min, s_avg
FROM empleados
WHERE dep_no = dep_numero;

END //
