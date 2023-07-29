program 'Fatorial';
Var
    count, count1, n, s: Integer;
    r: Real;
begin
    write('Você deseja descobrir o fatorial de quantos números? ');
    read(s);
    count1:= 0;
    repeat
        count1:= (count1 + 1);
        write('Que número você deseja descobrir o fatorial: ');
        read(n);
        count:= n;
        r:= 1;
        repeat
            r:= (r * count);
            count:= (count - 1);
        until (count < 1);
        writeln('o fatorial de ', n, ' é ', r, '.');
    until (count1 > (s - 1));
end.