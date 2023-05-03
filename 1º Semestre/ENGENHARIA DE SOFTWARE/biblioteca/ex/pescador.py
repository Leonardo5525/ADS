def pescador(x):
    p = float(input('Quantos quilos de peixe trouxe? '))
    excesso = p - 30
    multa = excesso * 3
    print(f'Senhor Zé você pescou {p} quilos de peixe.')
    print(f'Sendo o excedente {excesso} quilos, esses serão passíveis de multa por quilo a mais.')
    print(f'Em seu caso a multa será de {multa:.2f} reais. ')