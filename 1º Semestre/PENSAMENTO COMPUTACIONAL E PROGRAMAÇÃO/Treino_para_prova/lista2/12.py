n1 = float(input(f'Escolha um número: '))
simbolo = input('Escolha o tipo de operação: ')
n2 = float(input(f'Escolha um número: '))
total = 0

if simbolo == '+':
    total = n1 + n2
elif simbolo == '-':
    total = n1 - n2
elif simbolo == '/':
    total = n1 / n2
elif simbolo == '*':
    total = n1 * n2

print(f'O resultado é {total}')
