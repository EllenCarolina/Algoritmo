program 'ContarNumNeg';
Var
    count, s, m: Integer;
    n: Real;
begin
 	count:= 0;
 	m:= 0;
 	write('Quantos números você deseja contar: ');
 	read(s);
	repeat
	    write('Digite um número: ');
	    read(n);
		if (n < 0) then
		    m:= (m + 1);
		count:= (count + 1);
    until (count > (s - 1));
    write('Você digitou ', m, ' número(s) negativo(s).');
end.