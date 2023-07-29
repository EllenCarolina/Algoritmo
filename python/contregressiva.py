count = 0
soma = 0
maior = 0
menor = 8000000000000000000000000000000000000000000000000000000000
while count <= 9:
  count = count + 1
  print('Digite o '+ str(count) +'o. um número: ')
  num = int(input())
  if num > maior:
    maior = num
  if num < menor:
    menor = num
  soma = soma + num
print('A soma é: ', soma)
print('O maior número que você digitou foi:', maior)
print('O menor número que você digitou foi:', menor)