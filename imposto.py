produto = float(input('Qual o valor do produto? '))
imposto = float(produto * 0.6)
imposto = round(imposto, 2)
print('O imposto pago sobre o produto será de R$', imposto)