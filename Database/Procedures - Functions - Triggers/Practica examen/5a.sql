use procedimientos;
CREATE TABLE if not exists Productos (
 idProducto INT PRIMARY KEY,
 nombre VARCHAR(50),
 stock INT NOT NULL
);
CREATE TABLE if not exists Ventas (
 idVenta INT PRIMARY KEY,
 idProducto INT,
 cantidadVendida INT NOT NULL,
 FOREIGN KEY (idProducto)
REFERENCES Productos(idProducto)
);
drop procedure if exists StockAgotadoXXX;

delimiter //
create procedure StockAgotadoXXX(IN p_id INT, IN p_cantidad INT)
begin

DECLARE v_actual INT;
    SELECT stock INTO v_actual FROM Productos WHERE idProducto = p_id;

    IF v_actual < p_cantidad THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: No hay stock suficiente';
    END IF;
    
end //
delimiter ;
