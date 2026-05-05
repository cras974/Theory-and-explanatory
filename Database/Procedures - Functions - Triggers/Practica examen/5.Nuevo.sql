# 5.1

DELIMITER //
drop procedure if exists StockAgotadoXXX //
CREATE PROCEDURE StockAgotadoXXX (in p_ventas int, in p_stock int)

BEGIN

	if p_ventas > p_stock then
		signal sqlstate "45000" set message_text = "Las ventas son mayores que el stock";
	end if;

END //

DELIMITER ;

#5.2

DELIMITER //
DROP PROCEDURE IF EXISTS SinDatosXXX //
CREATE PROCEDURE SinDatosXXX ()
BEGIN

	if not exists (select * from Productos) and not exists (select * from ventas) then
		signal sqlstate "45001" set message_text = "Las dos tablas estan vacias";
	end if;
    
	if not exists (select * from Productos) then
		signal sqlstate "45002" set message_text = "La tabla productos esta vacia";
	end if;
    
	if not exists (select * from ventas) then
		signal sqlstate "45003" set message_text = "La tabla ventas esta vacia";
	end if;

END //

DELIMITER ;