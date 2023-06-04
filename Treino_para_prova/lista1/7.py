import math
metros = float(input('Quantos metros quadrados deverão ser pintados: '))
litros = math.ceil(metros / 3) 
lata = math.ceil(litros/18)
comprar = lata * 80

print(f'O número de latas a serem compradas é de {lata}')
print(f'O valor total é de {comprar}')
