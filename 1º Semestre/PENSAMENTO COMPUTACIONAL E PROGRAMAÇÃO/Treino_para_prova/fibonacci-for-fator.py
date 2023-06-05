fator = int(input('Escolha um limite para a sequencia: '))
n1 = 0
n2 = 1
total = 0

if fator == 0:
    exit

elif fator >= 1:
    print(0)
    print(1)
    for i in range(2,fator):
        total = n1 + n2
        print(total)
        n1 = n2
        n2 = total
    