def height():
    altura = float(input('Qual a sua altura = '))
    return altura**2

def weight():
    peso = float(input('Qual o seu peso = '))
    return peso

def imc():    
    imc = weight() / height()
    print(imc)