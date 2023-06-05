fator =  int(input('Escolha o valor para parar: '))
n1 = 0
n2 = 1
total = 0
lista = []

if fator == 0:
    exit
elif fator >= 1:
    lista.append(n1)
    lista.append(n2)

while fator > len(lista):
    total = n1 + n2
    lista.append(total)
    n1 = n2 
    n2 = total

print(lista)