('Bem vindo ao Mercadinho Bigbo')
i = 1
cont = 1
total = 0

while i != 0:
    i = float(input(f'Produto {cont}: R$ '))
    total += i
    cont += 1

print('-'*30)
print(f'Total: R${total}')
print('-'*30)

pagamento = float(input('Qual será sua quantia de pagamento: '))
print(f'Troco: R$ {pagamento - total}')