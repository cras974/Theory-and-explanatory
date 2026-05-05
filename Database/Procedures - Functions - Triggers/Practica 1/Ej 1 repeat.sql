DELIMITER //
CREATE PROCEDURE calcular_cuadrados(IN tope int unsigned)
BEGIN

	DECLARE i int default 1;
    
    TRUNCATE cuadrados;
    
	repeat
		insert into cuadrados values (i, i*i);
        set i = i + 1;
	until i > tope
	
    end repeat;
    
    select * from cuadrados;

END //

delimiter ;

CALL calcular_cuadrados (5);
