win = []
unix = []
lin = []
net = []
mac = []
outro = []
n = 0
i = 0
total = 0 
print('Qual o melhor sistema operacional para uso em servidores? ')

while True:
    n = input('''
----------------------------------
As possíveis respostas são:
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
0- sair
-----------------------------------
''' )
    if n == '1':
        win.append(n)
    elif n == '2':
        unix.append(n)
    elif n == '3':
        lin.append(n)
    elif n == '4':
        net.append(n)
    elif n == '5':
        mac.append(n)
    elif n == '6':
        outro.append(n)
    elif n == '0':
        break
    i += 1

total = len(win) + len(unix) + len(lin) + len(net) + len(mac) + len(outro)



print(f'''
Sistema Operacinal           Votos               %
------------------          -------             ----
Windows Server              {len(win)}\t\t\t{(len(win) * 100)/total}
Unix                        {len(unix)}\t\t\t{(len(unix) * 100)/total}
Linux                       {len(lin)}\t\t\t{(len(lin) * 100)/total} 
Netware                     {len(net)}\t\t\t{(len(net) * 100)/total}
Mac OS                      {len(mac)}\t\t\t{(len(mac) * 100)/total}
Outro                       {len(outro)}\t\t\t{(len(outro) * 100)/total}
------------------          --------            ------
Total                       {total}
''')