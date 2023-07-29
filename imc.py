massa = float(input('Qual é o seu peso (em kg): '))
altura = float(input('Qual a sua altura (em m): '))
imc = float(massa/(altura ** 2))
imc = round(imc, 2)
if 18.5 <= imc <= 25:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está com o peso ideal.')
else:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você não está com o peso ideal.')