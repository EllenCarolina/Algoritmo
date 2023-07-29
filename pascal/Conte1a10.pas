program 'Conte1a10';
Var
    count, n: Integer;
begin
 	count:= 1;
	write('Digite o número que deseja multiplicar: ')
	read(n)
	repeat
		writeln(count);
		count:= n * (count + 1);
  until (count > 10)
end.