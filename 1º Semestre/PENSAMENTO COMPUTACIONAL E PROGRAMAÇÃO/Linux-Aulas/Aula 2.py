sexo = input('Qual o seu sexo M/F? ').upper()
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura**2)
print(f'{imc:.2f}')
print(f'Uma pessoa de genêro {sexo}, {peso} kilos e {altura} metros')

if sexo == 'F' and imc >= 18.5 and imc <= 24.9:
    print('Peso considerado ideal')
elif sexo == 'F' and imc >= 25 and imc <= 29.9:
    print('Pessoa está acima do peso')
elif sexo == 'F' and imc >= 30 and imc <= 34.9:
    print('Obesidade de 1ª grau')
elif sexo == 'F' and imc >= 35 and imc <= 39.9:
    print('Obesidade de 2º grau')
elif sexo == 'F' and imc >= 40:
    print('Obesidade de 3º grau ou mórbida')
elif sexo == 'M' and imc <= 20.7:
    print('Abixo do peso')
elif sexo == 'M' and imc >= 20.7 and imc <= 26.4:
    print ('Peso considerado normal')
elif sexo == 'M' and imc >= 26.5 and imc <= 27.8:
    print('Um poco acima do peso')
elif sexo == 'M' and imc >= 27.9 and imc <= 31.1:
    print('Acima do peso')
elif sexo == 'M' and imc >= 31.2:
    print('Obesidade')



