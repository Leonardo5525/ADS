import random
lista = []

i = 0
while i < 10:
    valores = random.randint(1,10)
    lista.append(valores)
    i+=1

i=0
while i < len(lista):
    print(lista[i])
    i+=1

print('-'*30)

i = 9
while i > -1:
    print(lista[i])
    i-=1

'''
i = len(lista) - 1
while i > -1:
    print(lista[i])
    i-=1
'''