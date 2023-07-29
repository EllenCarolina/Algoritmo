program 'EscolhendoPessoas': 
Var
    idade, cor, cont_m, cont_h, continue: Integer;
    sexo: String;
begin
    repeat
        writeln('-----SELETOR DE PESSOAS-----');
        writeln('|    Qual o sexo? [F/M]    |');
        read(sexo);
        writeln('|      Qual a idade?       |');
        read(idade);
        writeln('|   Qual a cor do cabelo?  |');
        writeln('|       [1] Castanho       |');
        writeln('|        [2] Preto         |');
        writeln('|        [3] Loiro         |');
        writeln('|        [4] Ruivo         |');
        read(cor);
        cont_m:= 0;
        if (sexo = 'F') then
            begin
            if (idade > 25) and (idade < 30) then
                begin
                if (cor = 3) then
                    begin
                    cont_m:= (cont_m + 1);
                    end;
                end;
            end;
        cont_h:= 0;
        if (sexo = 'M') then
            begin
            if (idade > 18) then
                begin
                if (cor = 1) then
                    begin
                    cont_h:= (cont_h + 1);
                    end;
                end;
            end;
        writeln('Deseja continuar? [1(SIM)/2(NÃO)] ');
        read(continue);
    until (continue = 2);
    writeln('O total de mulheres entre 25 e 30 anos e cabelos loiros foi de: ', cont_m);
    writeln('O total de homens com mais de 18 anos e cabelos castanhos foi de: ', cont_h);
end.