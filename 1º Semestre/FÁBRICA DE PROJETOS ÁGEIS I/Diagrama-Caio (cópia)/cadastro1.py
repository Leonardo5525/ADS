qtd_usuarios = int(input('Quantos usuários deseja inserir? '))

usuario = []
senha = []

i = 0
while i <= qtd_usuarios:
    print('-------------------------------')
    print('-----Bem Vindo ao cadastro-----')
    nome = input('Digite seu usuário: ')
    abstrato = input('Digite sua senha: ')
    print('-------------------------------')

    usuario.append(nome)
    senha.append(abstrato)
    i = i + 1


print('--------------------------------')
print('---Faça o login de sua conta---')
print('--------------------------------')
user = (input('Digite o seu usuário: ')).strip()
pin = (input('Digite a sua senha: ')).strip()

checkUser = False
checkPass = False 
while user not in usuario:
    print('Usuário não encontrado!')
    user = (input('Digite o seu usuário: ')).strip()
else:
    checkUser = True

while pin not in senha:
    print('Senha incorreta!')
    pin = (input('Digite a sua senha: ')).strip()
else:
    checkPass = True

if checkUser and checkPass == True:
    print('--------------------------')
    print('----       MAPA        ----')
    print('----    NOTIFICAÇÕES   ----')
    print('----     CONVERSAS   ----')
