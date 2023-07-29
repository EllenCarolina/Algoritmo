program 'Multiplicacao';
Var
    count, n, r: Integer;
begin
 	count:= 1;
 	write('Digite o número que deseja multiplicar: ');
	read(n);
	repeat
		r:= (n * count);
		writeln(n, ' x ', count, ' = ', r);
		count:= (count + 1);
    until (count > 10)
end.