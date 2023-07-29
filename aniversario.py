ano = input('Em que ano nós estamos? ')
aniversario = input('Em que ano você nasceu? ')
idade = int(ano) - int(aniversario)
print('A sua idade é ' + str(idade) + ' anos em ' + str(ano) + '.')
if idade >= 21:
 print('E você já está na maioridade.')
else:
  print('E você ainda não está na maioridade.')