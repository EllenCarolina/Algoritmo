massa = float(input('Qual é o seu peso (em kg): '))
altura = float(input('Qual a sua altura (em m): '))
imc = float(massa/(altura ** 2))
imc = round(imc, 2)
if imc < 17:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está muito abaixo do peso.')
elif 17 < imc <= 18.5:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está abaixo do peso.')
elif 18.5 < imc <= 25:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está com o peso ideal.')
elif 25 < imc <= 30:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está com sobrepeso.')
elif 30 < imc <= 35:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está com obesidade.')
elif 35 < imc <= 40:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você está com obesidade severa.')
elif imc > 40:
  print('Seu peso é', massa, 'kg e sua altura é', altura, 'm, seu imc é', imc, 'e você não está com obesidade mórbida.')