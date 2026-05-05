DROP TRIGGER IF EXISTS tr_actualizar_stock;

DELIMITER //

CREATE TRIGGER tr_actualizar_stock
AFTER INSERT ON lineas_pedido
FOR EACH ROW
BEGIN
    UPDATE articulos 
    SET stock = stock - NEW.cantidad 
    WHERE id_articulo = NEW.id_articulo;
END //

DELIMITER ;