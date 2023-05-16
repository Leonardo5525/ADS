def area():
    a = float(input('Qual altura do local = '))
    l = float(input('Qual altura do local = '))     
    total = a * l
    return total

def tinta(cobertura):
    pintar = cobertura / 3
    return pintar

def finale():
    cobertura = area()
    arte = tinta(cobertura)
    pagar = arte*80
    print(pagar)

def acabou(a,l):
    area = a * l
    arte = area/3
    pagar = arte*80
    return pagar
