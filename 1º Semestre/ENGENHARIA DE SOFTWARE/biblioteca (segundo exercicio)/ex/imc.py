def imc():
    peso = float(input('Qual o seu peso = '))
    altura = float(input('Qual a sua altura = '))
    imc = peso / (altura * altura)
    print(imc)