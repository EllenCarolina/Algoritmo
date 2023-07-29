program 'VerificadordePrimo';
Var
    count, s, a: Integer;
    r: Real;
begin
    write('Digite um número: ');
    read(s);
    count:= 0;
    a:= 0;
    repeat
        count:= (count + 1);
        if (s mod count = 0) then
        begin
            a:= a + 1;
        end
    until (count > (s - 1));
    if (a > 2) then
    begin
        writeln('O número ', s,' não é primo.');
    end
    else
    begin
        writeln('O número ', s,' é primo.');
    end