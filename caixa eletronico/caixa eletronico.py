import os

saldo_atual = 1000

usuario = input("Informe sua conta: ")
senha = input("Informe sua senha: ")


def apagar_terminal():
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)


def buscar_saldo(nome_conta):
    try:
        with open("contas.txt", "r") as dados:
            for registro in dados:
                partes = registro.strip().split(";")

                if len(partes) == 2 and partes[0] == nome_conta:
                    return int(partes[1])

    except FileNotFoundError:
        pass

    return 1000


def calcular_notas(quantia):
    notas_disponiveis = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for nota in notas_disponiveis:
        quantidade = quantia // nota
        quantia %= nota

        if quantidade > 0:
            resultado[nota] = quantidade

    if quantia != 0:
        return None

    return resultado


def mostrar_saldo():
    print(f"\nSaldo disponível: R${saldo_atual},00")
    input("\nAperte ENTER para continuar.")


def realizar_saque():
    global saldo_atual

    try:
        quantia = int(input("Quanto deseja sacar? R$"))
    except ValueError:
        print("Erro: informe um valor inteiro.")
        input("Aperte ENTER para continuar.")
        return

    if quantia <= 0:
        print("Não é possível sacar esse valor.")

    elif quantia > saldo_atual:
        print(f"Saldo insuficiente. Disponível: R${saldo_atual},00")

    else:
        notas = calcular_notas(quantia)

        if notas is None:
            print("Não há cédulas disponíveis para esse valor.")
        else:
            saldo_atual -= quantia

            print("\nSaque efetuado com sucesso!")
            print("Cédulas a serem entregues:")

            for nota, quantidade in notas.items():
                print(f"{quantidade} cédula(s) de R${nota}")

            print(f"\nSaldo restante: R${saldo_atual},00")

    input("\nAperte ENTER para continuar.")


def realizar_deposito():
    global saldo_atual

    try:
        quantia = int(input("Quanto deseja depositar? R$"))
    except ValueError:
        print("Erro: informe um valor inteiro.")
        input("Aperte ENTER para continuar.")
        return

    if quantia < 1:
        print("O valor informado não é válido.")
    else:
        saldo_atual += quantia
        print(f"\nDepósito de R${quantia},00 realizado.")
        print(f"Saldo atualizado: R${saldo_atual},00")

    input("\nAperte ENTER para continuar.")


def salvar_dados(nome_conta, saldo):
    cadastro = {}

    try:
        with open("contas.txt", "r") as dados:
            for registro in dados:
                partes = registro.strip().split(";")

                if len(partes) == 2:
                    cadastro[partes[0]] = partes[1]

    except FileNotFoundError:
        pass

    cadastro[nome_conta] = saldo

    with open("contas.txt", "w") as dados:
        for nome, valor in cadastro.items():
            dados.write(f"{nome};{valor}\n")


saldo_atual = buscar_saldo(usuario)

print("\nBem-vindo ao Caixa Eletrônico!")

while True:
    apagar_terminal()

    print("===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Sacar dinheiro")
    print("3 - Depositar dinheiro")
    print("4 - Encerrar atendimento")

    escolha = input("\nDigite a opção desejada: ")

    if escolha == "1":
        mostrar_saldo()

    elif escolha == "2":
        realizar_saque()

    elif escolha == "3":
        realizar_deposito()

    elif escolha == "4":
        salvar_dados(usuario, saldo_atual)

        print("\nObrigado por utilizar nosso sistema!")
        print("Saldo salvo com sucesso.")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
        input("Aperte ENTER para continuar.")