limite =  int(input('Escolha o valor para parar: '))
n1 = 0
n2 = 1
total = 0
lista = []

if limite == 0:
    exit
elif limite >= 1:
    lista.append(n1)
    lista.append(n2)

while total < limite:
    total = n1 + n2

    if total > limite:
        break
    lista.append(total)
    n1 = n2 
    n2 = total

print(lista)
    