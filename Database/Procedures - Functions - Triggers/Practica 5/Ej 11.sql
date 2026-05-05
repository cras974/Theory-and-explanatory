CREATE TABLE historial_eliminados (
    id_articulo INT,
    nombre_articulo VARCHAR(100),
    precio DECIMAL(10,2),
    fecha_eliminacion DATETIME
);

DROP TRIGGER IF EXISTS tr_respaldo_eliminados;

DELIMITER //

CREATE TRIGGER tr_respaldo_eliminados
AFTER DELETE ON articulos
FOR EACH ROW
BEGIN
    INSERT INTO historial_eliminados (
        id_articulo, 
        nombre_articulo, 
        precio, 
        fecha_eliminacion
    ) 
    VALUES (
        OLD.id_articulo, 
        OLD.nombre, 
        OLD.precio, 
        NOW()
    );
END //

DELIMITER ;