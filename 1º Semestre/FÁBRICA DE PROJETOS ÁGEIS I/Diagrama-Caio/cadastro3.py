usuarios = []
senhas = []

while True:
  e = input('''
Ben vindo ao carona unimar!
[1] cadastrar usuario
[2] entrar
[3] listar
[0] sair
''')
  if e == '1':
    qtn_usuario = int(input('Quantidade: '))
    for i in range(qtn_usuario):
      usur = input('Usuario: ')
      paswd = input('Senha: ')
      usuarios.append(usur)
      senhas.append(paswd)
  elif e == '2':
    login = input('Usuario: ')
    senha = input('Senha: ')
    if (login in usuarios) and (senha in senhas):
      print('entrou')
    else:
      print('vaza')
  elif e == '3':
    print('-'*20)
    for i in usuarios:
      print(i)
  elif e == '0':
    break