print('--------------------------')
print('           IFGW           ')
print('--------------------------')
p1 = float(input('Digite a nota da sua primeira prova: '))
p2 = float(input('Digite a nota da sua segunda prova: '))
p = (p1 + p2)/2
if p <= 5:
  print('Sua média é', p)
  print('Seu aproveitamento é F')
elif 5 < p <= 6:
  print('Sua média é', p)
  print('Seu aproveitamento é E')
elif 6 < p <= 7:
  print('Sua média é', p)
  print('Seu aproveitamento é D')
elif 7 < p <= 8:
  print('Sua média é', p)
  print('Seu aproveitamento é C')
elif 8 < p <= 9:
  print('Sua média é', p)
  print('Seu aproveitamento é B')
elif 9 < p <= 10:
  print('Sua média é', p)
  print('Seu aproveitamento é A')