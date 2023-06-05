o = int(input('Informe o fatorial de: '))
print(f'Fatorial de {o}!')
i = 1
total = 0 

while i <= o:
    total = o * i
    i=i+1
    print(f'{o}, =, {i}', end='',)
