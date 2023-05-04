def metros():
    x = int(input(f'Escolha uma medida em metros = '))
    return x

def calculo(medida):
    return medida * 100

def metro_cent():
    medida = metros()
    cent = calculo(medida)
    print(f'{medida} metros será igual a {cent} centímetros.')