from ex.metro import metro_cent
from ex.salario import salario_mes
from ex.fh import fh
from ex.imc import imc
from ex.pescador import pescador
from ex.inss import inss

while True:
    e = input('''
    ----------------------------------
    Escolha o tipo de exercício que deseja fazer:
    [1] Metros
    [2] Salario
    [3] Farenheit
    [4] IMC
    [5] Pescador
    [6] INSS
    [0] sair
    -----------------------------------
    ''')
    if e == '1':
        metro_cent()
    elif e == '2':
        salario_mes()
    elif e == '3':
        fh()
    elif e == '4':
        imc()
    elif e == '5':
        pescador()
    elif e == '6':
        inss()
    elif e == '0':
        break