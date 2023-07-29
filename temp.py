temp_fahrenheit = float(input('Qual a temperatura atual? (em Fahrenheit) '))
temp_celsius = float(5 *((temp_fahrenheit - 32)/9))
temp_celsius = round(temp_celsius, 2)
print('A temperatura em Celsius é', temp_celsius)