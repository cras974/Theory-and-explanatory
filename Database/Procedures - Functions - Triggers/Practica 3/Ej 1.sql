/*Crea un procedimiento para la base de datos GIMNASIO que calcule el montante total de recibos pagados por cada usuario 
y lo almacene en una tabla auxiliar que tendrá los siguientes campos: nombre del usuario, fecha y total pagado*/

CREATE TABLE AUXILIAR (
    nombre_usuario VARCHAR(100),
    fecha_calculo DATE,
    total_pagado DECIMAL(10, 2)
);

DROP PROCEDURE CalcularMontanteUsuarios

DELIMITER //

CREATE PROCEDURE CalcularMontanteUsuarios()
BEGIN
    INSERT INTO RESUMEN_PAGOS (nombre_usuario, fecha_calculo, total_pagado)
    SELECT nombre,NOW(), SUM(importe)
	FROM USUARIOS JOIN RECIBOS USING (id_usuario)
    WHERE estado = 'Pagado'
    GROUP BY id_usuario;
END;

DELIMITER ;