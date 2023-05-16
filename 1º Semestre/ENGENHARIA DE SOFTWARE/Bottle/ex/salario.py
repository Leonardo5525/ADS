def valores():
    x = float(input(f'Qual é remuneração por hora = '))
    y = float(input(f'Quantas horas você trabalha por mês = '))
    return x, y

def calculos(x,y):
    return x * y

def salario_mes():
    x,y = valores()
    salario = calculos(x,y)

    print(f'Se você recebe {x} por hora, então seu salário será de {salario:.2f} R$ ')
