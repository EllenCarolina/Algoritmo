print('--------------------------')
print('    PALMEIRAS X VASCO     ')
print('--------------------------')
gp = int(input('Quantos gols o PALMEIRAS fez? '))
gv = int(input('Quantos gols o VASCO fez? '))
g = int(gp - gv)
g = abs(g)
match g:
  case 0:
    print('A diferença de gols foi:', g)
    print('Houve um Empate!')
  case 1, 2, 3, 4:
    print('A diferença de gols foi:', g)
    print('Partida Normal!')
  case _:
    print('A diferença de gols foi:', g)
    print('GOLEADA!')