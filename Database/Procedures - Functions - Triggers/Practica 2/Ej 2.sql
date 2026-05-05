/*Realiza un procedimiento llamado HallarNumEmp que recibiendo un nombre de departamento, 
muestre en pantalla el número de empleados de dicho departamento. Puedes utilizar la función creada en el ejercicio 1.*/

DROP PROCEDURE IF EXISTS HallarNumEmp

DELIMITER //

CREATE PROCEDURE HallarNumEmp (IN nombre varchar(50), OUT empleados INT)

BEGIN

	SET empleados = (SELECT COUNT(*) FROM empleados
					JOIN DEPARTAMENTOS USING (dep_no)
                    WHERE dnombre = nombre);

END //
DELIMITER ;

set @empleados = 0;
call empleados.HallarNumEmp('INVESTIGACION', @empleados);
select @empleados;
