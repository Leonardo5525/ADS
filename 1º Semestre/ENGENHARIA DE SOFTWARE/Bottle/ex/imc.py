def height():
    altura = float(input('Qual a sua altura = '))
    return altura

def weight():
    peso = float(input('Qual o seu peso = '))
    return peso

def imc(w,h):    
    imc = w / h**2
    return imc

def exercicio ():
    h = height()
    w = weight()
    r = imc(w,h)
    print(r)