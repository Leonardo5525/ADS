usuarios = []
senhas = []
i = 0

while True:
  e = input('''
----------------------------------
Bem vindo ao Unimar Park!
[1] cadastrar usuario
[2] entrar
[3] listar
[0] sair
----------------------------------1
''')
  if e == '1':
    qtn_usuario = int(input('Quantidade: '))
    while i < qtn_usuario:
      usur = input('Usuario: ')
      paswd = input('Senha: ')
      usuarios.append(usur)
      senhas.append(paswd)
      i += 1
  elif e == '2':
    login = input('Usuario: ')
    senha = input('Senha: ')
    if (login in usuarios) and (senha in senhas):
      print('entrou')
    else:
      print('Não possui cadastro')
  elif e == '3':
    print('-'*20)
    for i in usuarios:
      print(i)
  elif e == '0':
    break