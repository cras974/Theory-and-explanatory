DELIMITER //
drop function if exists ContarEmpleados //
create function ContarEmpleados (p_dpto varchar(20))
returns smallint unsigned
deterministic 

begin

	declare numerop smallint unsigned;
    set numerop=(SELECT count(*)
    from empleados join departamentos USING (dep_no)
    WHERE dnombre=p_dpto);
    
    return numerop;
    
end
//

delimiter ;

delimiter //

drop procedure if exists NumEmpleDPTO//

create procedure NumEmpleDPTO(IN p_dpt1 varchar(14), in p_dpt2 varchar(14))
begin

	declare emp1, emp2 smallint unsigned;
    
    set emp1=(SELECT ContarEmpleados(p_dpt1));
	set emp1=(SELECT ContarEmpleados(p_dpt2));
    
    SELECT emp1, emp2;

end

//

delimiter ; 

call NumEmpleDPTO('ventas','contabilidad')

delimiter //

drop function if exists comparar //
create function comparar(n int, m int)
returns varchar(20)
deterministic

begin

	if n < m then return concat(n,' es menor que ',m);
		
        elseif  n = m then return concat(n, ' es igual a ',m);
        
        else return concat(n, ' es mayor que ',m);
        
	end if;
        
end //

delimiter ;
select comparar(3,5);

delimiter //

drop procedure if exists comparar//
create procedure comparar(IN n int, in m int, out mensaje varchar(20) )
begin

	CASE 
		 WHEN n<m THEN SET mensaje = CONCAT(n, ' Es menor que ',m);
		 WHEN n=m THEN SET mensaje = CONCAT(n, ' Es igual que ',m);
		 ELSE SET mensaje = CONCAT(n, ' Es mayor que ',m);
	END CASE;
    
end //

delimiter ;

call comparar(5,9,@mensaje);
SELECT @mensaje;


-- Rellenar una tabla con los 10 primeros numeros

CREATE TABLE numeros (num int);

delimiter //

drop procedure if exists InsertarNum //
create procedure InsertarNum()
begin

	declare n int default 1;
    
	delete from numeros;
    
    miloop: loop
    
		if n > 10 then
        
			leave miloop;
        
        end if;
        
        insert into numeros values (n);
        set n = n + 1;
    
    end loop;´ç+

end //

delimiter ;
call insertarnum();
SELECT * FROM numeros;