from dataclasses import dataclass


@dataclass
class Socio:
    nome: str
    porce: float

def ler_socio(numero: int) -> Socio:
    print(f'Sócio de número {numero}')
    nome = input(f'Digite a o nome: ')
    porce = float(input(f'Digite a porcentagem que esse sócio possui: '))
    return Socio(nome, porce)

valor = float(input('Valor da empresa = '))

def porcentagem_Socio(porce: float, valor: float) -> float:
    porce = porce / 100
    resultado = valor * porce
    return resultado

so1 = ler_socio(1)
so2 = ler_socio(2)
so3 = ler_socio(3)

print(f'O socio {so1.nome} tem R$ {porcentagem_Socio(so1.porce,valor):.2f} de ações')
print(f'O socio {so2.nome} tem R$ {porcentagem_Socio(so2.porce,valor):.2f} de ações')
print(f'O socio {so3.nome} tem R$ {porcentagem_Socio(so3.porce,valor):.2f} de ações')
