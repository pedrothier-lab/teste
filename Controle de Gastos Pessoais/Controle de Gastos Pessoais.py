
import json
import os
from datetime import datetime

ARQUIVO = "movimentacoes.json"


# Carregar movimentações do arquivo JSON
def carregar_dados():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo, indent=4, ensure_ascii=False)
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        print("Erro ao carregar os dados.")
        return []


# Salvar movimentações no arquivo JSON
def salvar_dados(movimentacoes):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            movimentacoes,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# Adicionar receita ou despesa
def adicionar_movimentacao(movimentacoes, tipo):
    descricao = input("Descrição: ").strip()

    if descricao == "":
        print("A descrição não pode ficar vazia!")
        return

    try:
        valor = float(input("Valor: R$ ").replace(",", "."))

        if valor <= 0:
            print("O valor deve ser maior que zero!")
            return

    except ValueError:
        print("Digite um valor válido!")
        return

    # Gerar identificador automático
    if movimentacoes:
        novo_id = max(item["id"] for item in movimentacoes) + 1
    else:
        novo_id = 1

    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    movimentacao = {
        "id": novo_id,
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": data
    }

    movimentacoes.append(movimentacao)
    salvar_dados(movimentacoes)

    print(f"{tipo} cadastrada com sucesso!")


# Listar todas as movimentações
def listar_movimentacoes(movimentacoes):
    print("\n===== MOVIMENTAÇÕES =====")

    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

    for item in movimentacoes:
        print(
            f'{item["id"]} - {item["data"]} | '
            f'{item["tipo"]} | '
            f'R$ {item["valor"]:.2f} | '
            f'{item["descricao"]}'
        )


# Calcular saldo financeiro
def calcular_saldo(movimentacoes):
    saldo = 0

    for item in movimentacoes:
        if item["tipo"] == "Receita":
            saldo += item["valor"]
        elif item["tipo"] == "Despesa":
            saldo -= item["valor"]

    return saldo


# Consultar saldo
def consultar_saldo(movimentacoes):
    saldo = calcular_saldo(movimentacoes)

    print(f"\nSaldo atual: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))


# Excluir movimentação
def excluir_movimentacao(movimentacoes):
    listar_movimentacoes(movimentacoes)

    if not movimentacoes:
        return

    try:
        identificador = int(input("\nDigite o ID da movimentação que deseja excluir: "))

        for item in movimentacoes:
            if item["id"] == identificador:
                movimentacoes.remove(item)
                salvar_dados(movimentacoes)

                print("Movimentação excluída com sucesso!")
                return

        print("ID não encontrado!")

    except ValueError:
        print("Digite um identificador numérico válido!")


# Gerar relatório financeiro
def gerar_relatorio(movimentacoes):
    total_receitas = 0
    total_despesas = 0

    for item in movimentacoes:
        if item["tipo"] == "Receita":
            total_receitas += item["valor"]

        elif item["tipo"] == "Despesa":
            total_despesas += item["valor"]

    saldo = total_receitas - total_despesas

    print("\n===== RELATÓRIO FINANCEIRO =====")
    print(f"Total de Receitas: R$ {total_receitas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Total de Despesas: R$ {total_despesas:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Saldo Atual: R$ {saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print(f"Quantidade de Movimentações: {len(movimentacoes)}")


# Menu principal
def menu():
    movimentacoes = carregar_dados()

    print("Bem-vindo ao Controle de Gastos Pessoais!")

    while True:
        print("\n========== MENU ==========")
        print("1 - Adicionar Receita")
        print("2 - Adicionar Despesa")
        print("3 - Listar Movimentações")
        print("4 - Consultar Saldo")
        print("5 - Excluir Movimentação")
        print("6 - Gerar Relatório")
        print("0 - Sair")
        print("==========================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_movimentacao(movimentacoes, "Receita")

        elif opcao == "2":
            adicionar_movimentacao(movimentacoes, "Despesa")

        elif opcao == "3":
            listar_movimentacoes(movimentacoes)

        elif opcao == "4":
            consultar_saldo(movimentacoes)

        elif opcao == "5":
            excluir_movimentacao(movimentacoes)

        elif opcao == "6":
            gerar_relatorio(movimentacoes)

        elif opcao == "0":
            print("\nObrigado por utilizar o Controle de Gastos Pessoais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Executar o programa
menu()
