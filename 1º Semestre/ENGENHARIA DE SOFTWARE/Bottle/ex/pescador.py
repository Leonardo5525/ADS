def quilos():
    p = float(input('Quantos quilos de peixe trouxe? '))
    return p 

def passou(peso):
    return peso - 30

def pagar(excesso):
    return excesso * 3

def pescador():
    peso = quilos()
    excesso = passou (peso)
    multa = pagar(excesso) 
    print(f'Senhor Zé você pescou {peso} quilos de peixe.')
    print(f'Sendo o excedente {excesso} quilos, esses serão passíveis de multa por quilo a mais.')
    print(f'Em seu caso a multa será de {multa:.2f} reais. ')

def exer (kilo):
    limite = kilo - 30
    pagar = limite*3
    return pagar