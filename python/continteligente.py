print('------------------------------------------')
print('     BEM VINDO À CONTAGEM INTELIGENTE     ')
print('------------------------------------------')
inicio = int(input('Valor 1: '))
final = int(input('Valor 2: '))
if inicio < final:
  count = inicio
  print('------------------------')
  print('        CONTANDO        ')
  print('------------------------')
  while count <= final:
    print(count, '...')
    count = count + 1
elif inicio > final:
  count = inicio
  print('------------------------')
  print('        CONTANDO        ')
  print('------------------------')
  while count >= final:
    print(count, '...')
    count = count - 1