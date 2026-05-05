DROP PROCEDURE IF EXISTS Actualizar_stock;
DELIMITER //
CREATE PROCEDURE Actualizar_stock()
BEGIN
    DECLARE v_id INT;
    DECLARE v_cant INT;
    DECLARE fin INT DEFAULT false;
    
    -- El cursor es como un lector que va fila por fila en Ventas
    DECLARE cursor_v CURSOR FOR SELECT idProducto, cantidadVendida FROM Ventas;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = true;

    -- Paso 1: ¿Tablas vacías? (Si falla, aquí se para el programa)
    CALL SinDatosXXX();

    OPEN cursor_v;
    bucle: LOOP
        FETCH cursor_v INTO v_id, v_cant;
        
        IF fin THEN 
			LEAVE bucle; 
		END IF;

        -- Paso 2: ¿Hay stock para ESTA venta? (Si falla, aquí se para el programa)
        CALL StockAgotadoXXX(v_id, v_cant);

        -- Paso 3: Si todo está bien, restamos el stock
        UPDATE Productos SET stock = stock - v_cant WHERE idProducto = v_id;
        
    END LOOP;
    CLOSE cursor_v;
    
    SELECT '¡Todo actualizado con éxito!' AS Resultado;
END //
DELIMITER ;