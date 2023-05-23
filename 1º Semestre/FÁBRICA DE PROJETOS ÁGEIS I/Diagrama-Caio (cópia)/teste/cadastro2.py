cadastros = open ('cadastros.txt', 'a')
usuarios = []
senhas = []
i = 0
found = ''

while True:
  e = input('''
----------------------------------
Bem vindo ao Unimar Park!
[1] cadastrar usuario
[2] entrar
[3] listar
[0] sair
-----------------------------------
''')
  if e == '1':
    qtn_usuario = int(input('Quantidade: '))
    while i < qtn_usuario:
      usur = input('Usuario: ')
      paswd = input('Senha: ')
      usuarios.append(usur)
      senhas.append(paswd)
      #cadastros.write(f'{usur};{paswd}\n')
      cadastros.write(usur+';'+paswd)
      cadastros.write('\n')
      i += 1
  elif e == '2':
    login = input('Usuario: ')
    senha = input('Senha: ')
    cadastros = open('cadastros.txt', 'r')
    for cadastro in cadastros:
      usuario = (cadastro.strip()).split(';')
      #usuario = cadastro.split(';')
      print(usuario)
      if login == usuario[0] and senha == usuario[1]:
        found = True
        break
    if found == True:
      print('entrou')
    else:
      print('Não possui cadastro')
  elif e == '3':
    print('-'*20)
    for i in usuarios:
      print(i)
  elif e == '0':
    break