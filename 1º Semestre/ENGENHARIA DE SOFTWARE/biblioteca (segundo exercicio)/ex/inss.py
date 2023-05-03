def inss():
    x = float(input(f'Qual é remuneração por hora = '))
    y = float(input(f'Quantas horas você trabalha por mês = '))

    salario = x * y
    ir = salario * 0.11
    inss = (salario - ir) * 0.08
    sl = salario - (ir + inss)

    print(f'Se você recebe {x} por hora, então o seu salário burto será de {salario:.2f} R$ ')
    print(f'O valor do Imposto de Renda é de = {ir}')
    print(f'O valor do Imposto do INSS será de = {inss} ')
    print(f'Se você recebe {salario} R$ por mês, o seu total líquido após desconto de impostos sobrará {sl}')