numero = int(input("Digite um número inteiro: "))
fatorial = 1
i = 1

expressao = ""

print(f"Calculando o fatorial de {numero}:")


while i <= numero:
    fatorial *= i
    expressao += str(i)

    if i != numero:
        expressao += " * "
    else:
        expressao += " = "

    i += 1

print(f"{numero}! = {expressao}{fatorial}.")
