print('---------------------------')
print('          UNICAMP          ')
print('---------------------------')
alunos = int(input('Quantos alunos há na sua turma? '))
maior = 0
count = 0
nome1 = ''
while count <= (alunos - 1):
  count = count + 1
  print('---------------------------')
  print('          ALUNO', count, '          ')
  print('---------------------------')
  nome = input('Nome do(a) Aluno(a): ')
  print('Nota do(a)', nome, ':')
  nota = float(input())
  if nota > maior:
    maior = nota
    nome1 = nome
print('A melhor nota foi do(a) '+ nome1 +', com a nota '+ str(maior) +'.')