print('Departamento de trânsito')
ano = int(input('Ano atual (yyyy): '))
nasc = int(input('Ano de nascimento (yyyy): '))
if (ano - nasc) >= 18:
  print('Você tem', (ano - nasc), 'anos e por isso está apto à tirar a carteira para dirigir.')
else:
  print('Você tem', (ano - nasc), 'e por isso não está apto à tirar a carteira para dirigir.')