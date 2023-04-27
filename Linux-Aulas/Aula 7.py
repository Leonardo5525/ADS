valor = float(input('Qual o valor da compra = '))

d1 = valor - (valor *0.15)
d2 = valor - (valor *0.1)

if valor >= 600:
    print(f'A sua compra será custará {valor}, após o desconto de 15% {d1}')
else:
    print(f'A sua compra será custará {valor}, após o desconto de 10% {d2}')

