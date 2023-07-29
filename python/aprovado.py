print('Instituto de Física Gleb Wataghin')
n1 = float(input('Qual foi a sua nota na P1: '))
n2 = float(input('Qual foi a sua nota na P2: '))
n3 = float(input('Qual foi a sua nota na P3: '))
media = float((n1+n2+n3)/3)
media = round(media, 2)
if media >= 7.0:
  print('Média:', media)
  print('Você foi APROVADE!')
elif media < 5:
  print('Média:', media)
  print('Você está REPROVADE!')
else:
  print('Média:', media)
  print('Você tá de EXAME, meu chapa :(')