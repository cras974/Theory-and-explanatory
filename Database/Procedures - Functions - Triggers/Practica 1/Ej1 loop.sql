DELIMITER //
CREATE PROCEDURE calcular_cuadrados(IN tope int unsigned)
BEGIN

	DECLARE i int default 1;
    
    TRUNCATE cuadrados;
    
	my_loop:LOOP
		if i > tope then
			leave my_loop;
		end if;
        
        insert into cuadrados values (i, i*i);
        
        set i = i + 1;

END //

delimiter ;

CALL calcular_cuadrados (5);

SELECT * from cuadrados;