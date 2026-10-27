
import json
import os
from datetime import datetime

arquivo = "movimentacoes.json"


if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        movimentacoes = json.load(f)
else:
    movimentacoes = []



def salvar():
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(movimentacoes, f, indent=4, ensure_ascii=False)


while True:
    print("\n===== CONTROLE DE GASTOS =====")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Movimentacoes")
    print("4 - Consultar Saldo")
    print("5 - Excluir Movimentacao")
    print("6 - Gerar Relatorio")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1" or opcao == "2":
        descricao = input("Descricao: ")

        try:
            valor = float(input("Valor: ").replace(",", "."))
        except ValueError:
            print("Digite um valor valido!")
            continue

        if valor <= 0:
            print("O valor deve ser maior que zero!")
            continue

        if opcao == "1":
            tipo = "Receita"
        else:
            tipo = "Despesa"

        item = {
            "id": max([m["id"] for m in movimentacoes], default=0) + 1,
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        movimentacoes.append(item)
        salvar()
        print(tipo, "cadastrada com sucesso!")

    elif opcao == "3":
        if not movimentacoes:
            print("Nenhuma movimentacao cadastrada.")
        else:
            for m in movimentacoes:
                print(
                    m["id"], "-",
                    m["data"], "|",
                    m["tipo"], "| R$",
                    f'{m["valor"]:.2f}', "|",
                    m["descricao"]
                )

    elif opcao == "4":
        receitas = sum(
            m["valor"] for m in movimentacoes
            if m["tipo"] == "Receita"
        )

        despesas = sum(
            m["valor"] for m in movimentacoes
            if m["tipo"] == "Despesa"
        )

        print(f"Total de receitas: R$ {receitas:.2f}")
        print(f"Total de despesas: R$ {despesas:.2f}")
        print(f"Saldo atual: R$ {receitas - despesas:.2f}")

    elif opcao == "5":
        try:
            id_excluir = int(input("Digite o ID para excluir: "))
            encontrado = False

            for m in movimentacoes:
                if m["id"] == id_excluir:
                    movimentacoes.remove(m)
                    salvar()
                    print("Movimentacao excluida!")
                    encontrado = True
                    break

            if not encontrado:
                print("ID nao encontrado.")

        except ValueError:
            print("Digite um ID valido!")

    elif opcao == "6":
        receitas = sum(
            m["valor"] for m in movimentacoes
            if m["tipo"] == "Receita"
        )

        despesas = sum(
            m["valor"] for m in movimentacoes
            if m["tipo"] == "Despesa"
        )

        print("\n===== RELATORIO =====")
        print(f"Total de receitas: R$ {receitas:.2f}")
        print(f"Total de despesas: R$ {despesas:.2f}")
        print(f"Saldo atual: R$ {receitas - despesas:.2f}")
        print(f"Movimentacoes: {len(movimentacoes)}")

    elif opcao == "0":
        print("Obrigado por utilizar o programa!")
        break

    else:
        print("Opcao invalida!")