print("Digite nomes (pressione Enter em branco para terminar): ")
nomes = []
while True:
    nome = input("Digite o nome: ").strip()
    if nome == "":
        break
    nomes.append(nome)

with open("nomes.txt", "w", encoding="utf-8") as f:
    for n in nomes:
        f.write(n + "\n")