def valores():
    x = float(input(f'Qual é remuneração por hora = '))
    y = float(input(f'Quantas horas você trabalha por mês = '))
    return x * y

def imposto(salario):
    return salario * 0.11

def calculo(salario, ir):
    return (salario - ir) * 0.08

def salario_liquido (salario, ir, inss):
    return salario - (ir + inss)

def inss():
    salario = valores()
    ir = imposto(salario)
    inss = calculo (salario, ir)
    sl = salario_liquido (salario, ir, inss)

    print(f'O seu salário burto será de {salario:.2f} R$ ')
    print(f'O valor do Imposto de Renda é de = {ir}')
    print(f'O valor do Imposto do INSS será de = {inss} ')
    print(f'Se você recebe {salario} R$ por mês, o seu total líquido após desconto de impostos sobrará {sl}')

def final(x,y):
    salario = x * y
    ir = imposto(salario)
    inss = calculo (salario, ir)
    sl = salario_liquido (salario, ir, inss)
    return f'O seu salário burto será de {salario:.2f} R$. <br> O valor do Imposto de Renda é de = {ir}. <br> O valor do Imposto do INSS será de = {inss}. <br> Se você recebe {salario} R$ por mês, o seu total líquido após desconto de impostos sobrará {sl}.'