program 'Contagem SuperInteligente';
Var
    count, n: Integer;
begin
    repeat
    writeln('------------MENU------------');
    writeln('|[1] Para contar de 1 a 10. |');
    writeln('|[2] Para contar de 10 a 1. |');
    writeln('|[3] Para sair.             |');
    read(n);
    case n of
        1: begin
            count:= 0;
            repeat
                count:= (count + 1);
                writeln(count, '...');
            until (count >= 10);
        end;
        2: begin
            count:= 10;
            repeat
                writeln(count, '...');
                count:= (count - 1);
            until (count <= 0);
        end;
        3: begin
        end;
    end;
    until (n = 3);
end.