c = 1
cont_m = 0
cont_h = 0
while (c <= 1):
  print('-----SELETOR DE PESSOAS-----')
  sexo = str(input('|    Qual o sexo? [H/M]    |'))
  idade = int(input('|      Qual a idade?       |'))
  print('|   Qual a cor do cabelo?  |')
  print('|       [1] Castanho       |')
  print('|        [2] Preto         |')
  print('|        [3] Loiro         |')
  print('|        [4] Ruivo         |')
  cor = int(input())
  if sexo == 'M':
    if (idade >= 25) and (idade <= 30):
      if cor == 3:
        cont_m = (cont_m + 1)
  if sexo == 'H':
    if (idade > 18):
      if cor == 1:
        cont_h = (cont_h + 1)
  print('Deseja continuar? [1(Sim)/2(Não)] ')
  c = int(input())
print('O total de mulheres entre 25 e 30 anos e cabelos loiros foi de: ', cont_m)
print('O total de homens com mais de 18 anos e cabelos castanhos foi de: ', cont_h)