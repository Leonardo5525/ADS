{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyN50eIo61ry3zKqCvhK87K0"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["idade = int(input('Qual a sua idade para entrar no site da Ambev? '))\n","if idade >= 18:\n","    print('Liberado')\n","else:\n","    print('Ainda não pode')\n"],"metadata":{"id":"ImNnpLOawgVB"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["idade = int(input('Informe a sua idade = '))\n","\n","if idade >= 18:\n","    print('Seja Bem vindo\\nVocê passou na Ambev')\n","else:\n","    print('Você ainda não tem permissão\\nSinto muito')\n"],"metadata":{"id":"gPY_CmdSwB1_"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["altura = float(input('Qual é sua altura? '))\n","peso = float(input('Qual o seu peso? '))\n","idade = int(input('Qual a sua idade? '))\n","\n","if idade >= 18:\n","    print('Maior de idade')\n","else:\n","    print('Menor de idade')\n","if peso >= 90:\n","    print(f'{peso} = pesado')\n","else:\n","    print (f'{peso} = leve')\n","print(peso)\n"],"metadata":{"id":"hxt3lohPwHfQ"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["a = float(input('Escolha um número = '))\n","b = float(input('Escolha um número = '))\n","\n","if a > b:\n","    print(f'{a} maior número')\n","else:\n","    print(f'{b} menor número')\n"],"metadata":{"id":"VGqNdSL-wLXB"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["a = float(input('Escolha um número = '))\n","b = float(input('Escolha um número = '))\n","\n","if a < b:\n","    print(f'A = {a} menor número')\n","else:\n","    print(f'B = {b} menor número')\n"],"metadata":{"id":"sWyW5MZrwPkw"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["valor = float(input('Qual o valor da compra = '))\n","\n","d1 = valor - (valor *0.15)\n","d2 = valor - (valor *0.1)\n","\n","if valor >= 600:\n","    print(f'A sua compra será custará {valor}, após o desconto de 15% {d1}')\n","else:\n","    print(f'A sua compra será custará {valor}, após o desconto de 10% {d2}')\n"],"metadata":{"id":"UzLaaI6qwUj2"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["nasceu = int(input('Quando você nasceu? '))\n","ano = int(input('Que ano estamos? '))\n","\n","idade = ano - nasceu\n","\n","if idade >= 18:\n","    print('Você está apto paravotar.')\n","else:\n","    print('Logo mais meu jovem.')\n"],"metadata":{"id":"iANKx1COwXcA"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["a = int(input('Escolha um número '))\n","\n","if a >= 0:\n","    print('Núemro é positivo')\n","else:\n","    print('Número é negativo')\n"],"metadata":{"id":"TXPVV0bwwaa1"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["sexo = input('Qual o seu sexo M/F? ').upper()\n","peso = float(input('Qual é o seu peso? '))\n","altura = float(input('Qual a sua altura? '))\n","\n","imc = peso / (altura**2)\n","print(f'{imc:.2f}')\n","print(f'Uma pessoa de genêro {sexo}, {peso} kilos e {altura} metros')\n","\n","if sexo == 'M':\n","  if imc >= 40:\n","    print('Obesidade de 3º grau ou mórbida')\n","  elif imc >= 35:\n","    print('Obesidade de 2º grau')\n","  elif imc >= 30:\n","    print('Obesidade de 1ª grau')\n","  elif imc >= 25:\n","    print('Pessoa está acima do peso')\n","  elif imc >= 18.5:\n","    print('Peso considerado ideal')\n","\n","elif sexo == 'F':\n","  if imc >= 31.2:\n","    print('Obesidade')\n","  elif imc >= 27.9:\n","    print('Acima do peso')\n","  elif imc >= 26.5:\n","    print('Um poco acima do peso') \n","  elif imc >= 20.7:\n","    print('Abixo do peso')\n","\n","else:\n","  print(\"Informe um sexo válido\")"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"4upkBFbu-0li","executionInfo":{"status":"ok","timestamp":1677721757186,"user_tz":180,"elapsed":9450,"user":{"displayName":"Leonardo Nakamura","userId":"18017426429312993572"}},"outputId":"315ceaae-e257-435c-b5cd-60f9206255c0"},"execution_count":6,"outputs":[{"output_type":"stream","name":"stdout","text":["Qual o seu sexo M/F? m\n","Qual é o seu peso? 95\n","Qual a sua altura? 1.78\n","29.98\n","Uma pessoa de genêro M, 95.0 kilos e 1.78 metros\n","Pessoa está acima do peso\n"]}]},{"cell_type":"code","execution_count":5,"metadata":{"id":"o1qpyMYwvFGe","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1677721121810,"user_tz":180,"elapsed":19952,"user":{"displayName":"Leonardo Nakamura","userId":"18017426429312993572"}},"outputId":"0541b15f-4bff-46a2-d27e-d8144884d888"},"outputs":[{"output_type":"stream","name":"stdout","text":["Qual o seu sexo M/F? M\n","Qual é o seu peso? 95\n","Qual a sua altura? 1.78\n","29.98\n","Uma pessoa de genêro M, 95.0 kilos e 1.78 metros\n","Vocẽ desistiu, eu compreendo, está com vergonha\n"]}],"source":["sexo = input('Qual o seu sexo M/F? ').upper()\n","peso = float(input('Qual é o seu peso? '))\n","altura = float(input('Qual a sua altura? '))\n","\n","imc = peso / (altura**2)\n","print(f'{imc:.2f}')\n","print(f'Uma pessoa de genêro {sexo}, {peso} kilos e {altura} metros')\n","\n","if sexo == 'M' and imc >= 40:\n","    print('Obesidade de 3º grau ou mórbida')\n","elif sexo == 'M' and imc >= 35:\n","    print('Obesidade de 2º grau')\n","elif sexo == 'M' and imc >= 30:\n","    print('Obesidade de 1ª grau')\n","elif sexo == 'M' and imc >= 25:\n","    print('Pessoa está acima do peso')\n","elif sexo == 'M' and imc >= 18.5:\n","    print('Peso considerado ideal')\n","elif sexo == 'F' and imc >= 31.2:\n","    print('Obesidade')\n","elif sexo == 'F' and imc >= 27.9:\n","    print('Acima do peso')\n","elif sexo == 'F' and imc >= 26.5:\n","    print('Um poco acima do peso')        \n","elif sexo == 'F' and imc <= 20.7:\n","    print('Abixo do peso')\n","\n","\n","\n","\n","\n"]},{"cell_type":"code","source":["velo = int(input('Qual a velocidade que passou no radar? '))\n","limite = int(input('Qual o limite de velocidade da pista? '))\n","\n","multa = 500\n","ex = (velo - limite)/100\n","\n","if ex >= 0.5:\n","    total = multa*3\n","    print(f'A multa terá um aumento de 50%, sendo o total {total}')\n","elif ex >= 0.4:\n","    desc = multa - multa*0.01\n","    print(f'A multa terá 1% de desconto, sendo o total {desc}')\n","elif ex >= 0.3:\n","    desc = multa - multa*0.05\n","    print(f'A multa terá 7% de desconto, sendo o total {desc}')\n","elif ex >= 0.2:\n","    desc = multa - multa*0.07\n","    print(f'A multa terá 5% de desconto, sendo o total {desc}')\n","elif ex >= 0.:\n","    total = multa + multa*0.10\n","    print(f'A multa terá 1% de desconto, sendo o total {desc}')\n","elif velo < limite:\n","    print('Não haverá multa')"],"metadata":{"id":"4DORriwrv8qf","colab":{"base_uri":"https://localhost:8080/"},"executionInfo":{"status":"ok","timestamp":1677720438296,"user_tz":180,"elapsed":11465,"user":{"displayName":"Leonardo Nakamura","userId":"18017426429312993572"}},"outputId":"06731cc3-4c0b-41ee-ef13-93550b2dd7fd"},"execution_count":4,"outputs":[{"output_type":"stream","name":"stdout","text":["Qual a velocidade que passou no radar? 120\n","Qual o limite de velocidade da pista? 100\n","A multa terá 1% de desconto, sendo o total 495.0\n"]}]},{"cell_type":"code","source":["velo = int(input('Qual a velocidade que passou? '))\n","limite = int(input('Qual o limite da velocidade? '))\n","\n","ex = (velo - limite)/100\n","multa= 500\n","\n","\n","if ex >= 0.5:\n","    total = multa * 3\n","    print(f'Multa = {total}')\n","else:\n","    if ex < 0.5 and ex >= 0.4:\n","            total = multa - (multa*0.01)\n","    else:        \n","        if ex < 0.4 and ex >= 0.3:\n","            total = multa - (multa*0.05)\n","        else:    \n","            if ex < 0.3 and ex >= 0.2:\n","                total = multa - (multa*0.07)\n","            else:\n","                if ex < 0.2 and ex >= 0.1:\n","                    total = multa - (multa*0.1)\n","               \n","print(f'Multa = {total}') "],"metadata":{"id":"3Bl02gmQwAK8"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":[],"metadata":{"id":"7dKAJsBXwAmC"},"execution_count":null,"outputs":[]}]}