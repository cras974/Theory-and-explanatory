drop procedure if exists SinDatosXXX;

delimiter //
create procedure SinDatosXXX()
begin

    IF (SELECT COUNT(*) FROM Productos) = 0 OR (SELECT COUNT(*) FROM Ventas) = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERROR: No hay datos para trabajar';
    END IF;
    
end //
delimiter ;