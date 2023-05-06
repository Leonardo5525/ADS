i = 0

while i < 11:
    print(i)
    i+=1


limite = int(input('Escolha um valor limite = '))
i = 0
while i < limite:
    print(i)
    i += 1


i = 0
while i < 101:
    if i%2 == 0:
        print(i)
    i += 1


o = int(input('Escolha um valor e sua tabuada será mostrada = '))
i = 0
while i < 11:
    print('A tabuada desse valor é de:')
    print(f'{o} X {i} = {o*i}')
    i += 1

fatorial = 1
o = int(input('Informe o fatorial de: '))
print(f'Fatorial de {o}:')
print(f'{o}! =', end='')

while o > 0:
    fatorial *= o
    if o != 1:
        print(f'{o}', end='')
    else:
        print(f'{o}, =, {fatorial}', end='')




('Bem vindo ao Mercadinho Bigbo')
i = 1
total = 0

while i != 0:

    o = float(input(f'Produto {i}: R$ '))
    total += o
    i+=1

print('-'*30)
print(f'Total: R${total}')
print('-'*30)

pagamento = float(input('Qual será sua quantia de pagamento: '))
print(f'Troco: R$ {pagamento - pagamento}')



lista = [0,1,2,3,4]

i= 0 
while i < len(lista):
    print(i) 
    i +=1 


import random
lista = []
par = []
impar = []
i = 0

while i < 20:
    a = random.randint(0,100)
    lista.append(a)

    if a%2 == 0:
        par.append(a)
    else:
        impar.append(a)
    
    i +=1
