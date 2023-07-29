print('--------------------------')
print('    CRIANÇA ESPERANÇA     ')
print('--------------------------')
print('Digite [1] para doar R$10,00.')
print('Digite [2] para doar R$25,00.')
print('Digite [3] para doar R$50,00.')
print('Digite [4] para doar outros valores.')
print('Digite [5] para calcelar.')
tec = int(input())
match tec:
  case 1:
    valor = 10
  case 2:
    valor = 25
  case 3:
    valor = 50
  case 4:
    valor = float(input('Digite um valor: '))
  case 5:
    valor = 0
  case _:
    print('Não é um valor válido.')
print('Sua doação foi de R$'+ str(valor))