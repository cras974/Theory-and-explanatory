DELIMITER //
CREATE PROCEDURE calcular_cuadrados(IN tope int unsigned)
BEGIN

	DECLARE i int default 1;
    
    TRUNCATE cuadrados;
    
    WHILE i <= tope do
		insert into cuadrados values (i, i*i);
        set i = i+1;
	end while;

END //

delimiter ;

CALL calcular_cuadrados (20);

SELECT * from cuadrados;