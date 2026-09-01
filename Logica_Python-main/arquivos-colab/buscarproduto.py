produtos = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.30,
    "Feijão": 1.50,
    "Coca": 10.90,
}

pergunta = input("Qual produto você quer? ")
if pergunta in produtos:
  print(f"O preço de {pergunta} é {produtos[pergunta]}")
else:
  print("Produto não encontrado.")
