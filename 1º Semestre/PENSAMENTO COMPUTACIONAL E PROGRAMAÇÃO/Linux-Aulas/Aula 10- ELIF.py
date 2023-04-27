velo = int(input('Qual a velocidade que passou no radar? '))
limite = int(input('Qual o limite de velocidade da pista? '))

multa = 500
ex = (velo - limite)/100

if ex >= 0.1 and ex < 0.2:
    desc = multa - multa*0.1
    print(f'A multa terá 10% de desconto, sendo o total {desc}')
elif ex >= 0.2 and ex < 0.3:
    desc = multa - multa*0.07
    print(f'A multa terá 7% de desconto, sendo o total {desc}')
elif ex >= 0.3 and ex < 0.4:
    desc = multa - multa*0.05
    print(f'A multa terá 5% de desconto, sendo o total {desc}')
elif ex >= 0.4 and ex < 0.5:
    desc = multa - multa*0.01
    print(f'A multa terá 1% de desconto, sendo o total {desc}')
elif ex >= 0.5:
    total = multa + multa*3
    print(f'A multa terá um aumento de 50%, sendo o total {total}')
elif velo < limite:
    print('Não haverá multa')




