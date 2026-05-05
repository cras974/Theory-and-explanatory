DELIMITER //
DROP PROCEDURE IF EXISTS ObtenerClientePorID;
CREATE PROCEDURE ObtenerClientePorID (IN p_cliente_id CHAR(10), OUT p_nombre VARCHAR(30))
BEGIN
	SET p_nombre = (SELECT CONCAT(nombre,' ',apellido) 
					FROM CLIENTES 
                    WHERE idcliente = p_cliente_id);
END //
DELIMITER ;