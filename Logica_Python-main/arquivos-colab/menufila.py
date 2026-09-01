fila = []
historico = []
usuarios = {}

while True:

    acao = int(input("----- MENU -----\n\n(1) - Adicionar Cliente\n(2) - Atender cliente\n(3) - Mostrar fila\n(4) - Mostrar histórico\n(5) - Buscar cliente\n(6) - Sair.\n\nOque deseja fazer? "))

    if acao == 1:
      nome = (input("Digite o nome do cliente: "))
      idade = int(input(f"Digite a idade de {nome}: "))
      usuarios[nome] = idade
      cliente = {"nome": nome, "idade": idade}
      fila.append(cliente)
      print("Cliente adicionado à fila!")

    elif acao == 2:
      if not fila:
        print("Fila vazia!")
      else:
        cliente = fila.pop(0)
        print(f"Atendendo: {cliente['nome']}, {cliente['idade']} anos")
        historico.append(cliente)


    elif acao == 3:
      if not fila:
        print("Fila vazia.")
      else:
        for i in fila:
          print(f"{i['nome']}, {i['idade']} anos")

    elif acao == 4:
      if not historico:
        print("O histórico está vazio.")
      else:
        for i in historico:
          print(f"{i['nome']}, {i['idade']} anos")

    elif acao ==5:
      if not fila and not historico:
        print("Cliente não cadastrado.")
      else:
        nome_busca = input("Digite o nome do usuario: ")
        encontrado = False
        for i in fila:
          if i['nome'].lower() == nome_busca.lower():
            print("Cliente está na fila.")
            encontrado = True

        for i in historico:
            if i['nome'].lower() == nome_busca.lower():
              print("Cliente ja foi atendido.")
              encontrado = True
        if not encontrado:
            print("Cliente não encontrado.")

    elif acao == 6:
      break
