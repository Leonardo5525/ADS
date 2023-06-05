hora = float(input('Quanto você recebe por hora: '))
trabalha = int(input('Quantas hora você trabalha por mês: '))

salario = hora * trabalha
ir = salario * 0.11
inss = salario * 0.08
total = salario - ir - inss

print(salario)
print(ir)
print(inss)
print(total)
