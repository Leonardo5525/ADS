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
if user in usuario:
    pin = (input('Digite a sua senha: ')).strip()
    if pin in senha:
        print('--------------------------')
        print('----       MAPA        ----')
        print('----    NOTIFICAÇÕES   ----')
        print('----     CONVERSAS   ----')
    else:
        print('Senha incorreta tente novamente')
        pin = (input('Digite a sua senha: ')).strip()
else:
    print('Usuário incorreto tente novamente')
    user = (input('Digite o seu usuário: ')).strip()
    pin = (input('Digite a sua senha: ')).strip()
    if pin in senha:
        print('--------------------------')
        print('----       MAPA        ----')
        print('----    NOTIFICAÇÕES   ----')
        print('----     CONVERSAS   ----')
    else:
        print('Senha incorreta tente novamente')
        pin = (input('Digite a sua senha: ')).strip()
        if pin in senha:
            print('--------------------------')
            print('----       MAPA        ----')
            print('----    NOTIFICAÇÕES   ----')
            print('----     CONVERSAS   ----')



