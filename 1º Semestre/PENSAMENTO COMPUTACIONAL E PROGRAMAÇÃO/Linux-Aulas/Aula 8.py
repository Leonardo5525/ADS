nasceu = int(input('Quando você nasceu? '))
ano = int(input('Que ano estamos? '))

idade = ano - nasceu

if idade >= 18:
    print('Você está apto paravotar.')
else:
    print('Logo mais meu jovem.')