def salario_mes():
    x = float(input(f'Qual é remuneração por hora = '))
    y = float(input(f'Quantas horas você trabalha por mês = '))

    salario = x * y

    print(f'Se você recebe {x} por hora, então seu salário será de {salario:.2f} R$ ')
