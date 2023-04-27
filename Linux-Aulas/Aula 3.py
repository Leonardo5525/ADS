altura = float(input('Qual é sua altura? '))
peso = float(input('Qual o seu peso? '))
idade = int(input('Qual a sua idade? '))

if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
if peso >= 90:
    print(f'{peso} = pesado')
else:
    print (f'{peso} = leve')
print(peso)