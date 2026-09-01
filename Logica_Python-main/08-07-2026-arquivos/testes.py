# Carrega os filmes do arquivo para uma lista de dicionários
filmes = []

try:
    with open("filmes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            # Remove espaços e quebras de linha, e divide pelos pontos e vírgulas
            dados = linha.strip().split(";")
            if len(dados) == 4:  # Garante que a linha tem todos os dados
                filmes.append({
                    "titulo": dados[0].strip(),
                    "diretor": dados[1].strip(),
                    "genero": dados[2].strip(),
                    "duracao": int(dados[3].strip())  # Converte duração para número
                })
except FileNotFoundError:
    print("Erro: O arquivo 'filmes.txt' não foi encontrado.")
    print("Crie o arquivo com o formato: Título;Diretor;Gênero;Duração")

# Menu Interativo
while True:
    print("\n--- Menu Interativo ---")
    print("1. Quantidade total de filmes.")
    print("2. Informações de um filme pelo título.")
    print("3. Filmes de um diretor específico.")
    print("4. Filmes de um gênero específico.")
    print("5. Média de duração dos filmes.")
    print("6. Sair.")
    
    try:
        acao = int(input("Escolha a opção (utilize apenas números): "))
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
        continue

    if acao == 1:
        print(f"\nQuantidade total de filmes: {len(filmes)}")

    elif acao == 2:
        busca = input("Digite o título do filme: ").strip().lower()
        encontrado = False
        for f in filmes:
            if busca in f["titulo"].lower():
                print(f"\nTítulo: {f['titulo']} | Diretor: {f['diretor']} | Gênero: {f['genero']} | Duração: {f['duracao']} min")
                encontrado = True
        if not encontrado:
            print("Nenhum filme encontrado com esse título.")
    
    elif acao == 3:
        busca = input("Digite o diretor: ").strip().lower()
        encontrado = False
        print(f"\nFilmes dirigidos por '{busca}':")
        for f in filmes:
            if busca in f["diretor"].lower():
                print(f"- {f['titulo']} ({f['duracao']} min)")
                encontrado = True
        if not encontrado:
            print("Nenhum filme encontrado para este diretor.")

    elif acao == 4:
        busca = input("Digite o gênero do filme: ").strip().lower()
        encontrado = False
        print(f"\nFilmes do gênero '{busca}':")
        for f in filmes:
            if busca in f["genero"].lower():
                print(f"- {f['titulo']} (Diretor: {f['diretor']})")
                encontrado = True
        if not encontrado:
            print("Nenhum filme encontrado para este gênero.")

    elif acao == 5:
        if filmes:
            total_duracao = sum(f["duracao"] for f in filmes)
            media = total_duracao / len(filmes)
            print(f"\nMédia de duração dos filmes: {media:.2f} minutos.")
        else:
            print("\nNenhum filme cadastrado para calcular a média.")
    
    elif acao == 6:
        print("Saindo do programa... Até logo!")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 6.")
