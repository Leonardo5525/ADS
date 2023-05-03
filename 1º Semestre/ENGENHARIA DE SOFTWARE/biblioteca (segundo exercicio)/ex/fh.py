def temp_fh():
    f = float(input('Qual é a temperatura ai nos USA? '))
    return f

def calculo(temperatura):
    c = 5 * ((temperatura-32)/9)
    return c

def mensagem (conversao):
    print(f'Fazendo a conversão Fahrenheit para Celsius será igual {conversao} Cº')

def fh():
    temperatura = temp_fh()
    conversao = calculo(temperatura)
    mensagem(conversao)