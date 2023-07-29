c = 0
while (c < 3):
  print('------------------------------')
  print('             MENU             ')
  print('------------------------------')
  print('|[1] Para contar de 1 a 10.   |')
  print('|[2] Para contar de 10 a 1.   |')
  print('|[3] Para sair.               |')
  c = int(input())
  match c:
    case 1:
      count = 1
      while (count <= 10):
        print(count, '...')
        count = (count + 1)
    case 2:
      count = 10
      while (count >= 1):
        print(count, '...')
        count = (count - 1)
    case 3:
      print('Saindo...')