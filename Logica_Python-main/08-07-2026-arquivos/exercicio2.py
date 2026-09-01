with open("filmes.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
quantidade_filmes = conteudo.count("Titulo:")

def buscar_filme_por_titulo(titulo_buscado, nome_arquivo="filmes.txt"): 
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    blocos_de_filmes = conteudo.strip().split("\n\n")
    for bloco in blocos_de_filmes:
        if titulo_buscado.lower() in bloco.lower():
            return bloco     
    return "Filme não encontrado."

def buscar_por_diretor(diretor_buscado, nome_arquivo="filmes.txt"):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    bloco_de_filmes = conteudo.strip().split("\n\n")
    encontrados = []
    for bloco in bloco_de_filmes:
        if diretor_buscado.lower() in bloco.lower():
            encontrados.append(bloco)       
    if encontrados:
        return "\n\n---\n\n".join(encontrados)
    return "Diretor não encontrado"

def buscar_por_genero(genero_buscado, nome_arquivo="filmes.txt"):
    genero_buscado = genero_buscado.replace("ífica", "íifca")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    bloco_de_filmes = conteudo.strip().split("\n\n")
    encontrados = []
    for bloco in bloco_de_filmes:
        if genero_buscado.lower() in bloco.lower():
            encontrados.append(bloco)       
    if encontrados:
        return "\n\n---\n\n".join(encontrados)
    return "Gênero não encontrado"

def calcular_media_duracao(nome_arquivo="filmes.txt"):
    soma_duracao = 0
    total_filmes_duracao = 0
    
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.startswith("Duração:"):
                texto_minutos = linha.replace("Duração:", "").replace("Minutos", "").strip()
                soma_duracao += int(texto_minutos)
                total_filmes_duracao += 1
                
    if total_filmes_duracao > 0:
        media = soma_duracao / total_filmes_duracao
        return f"A média de duração dos filmes é de {media:.1f} minutos."
    return "Nenhum filme com duração encontrado no arquivo."

while True:
    print("\n - - - Menu interativo - - -")
    acao = int(input("1. Quantidade total de fimes.\n" \
    "2. Informações de um filme pelo o titulo.\n" \
    "3. Filmes de um diretor específico.\n" \
    "4. Filmes de um gênero especifico.\n" \
    "5. Média de duração dos filmes.\n" \
    "6. Sair.\n" \
    "Escolha a opção (utilize apenas números): "))

    if acao == 1:
        print(f"Total de filmes: {quantidade_filmes}")

    elif acao == 2:
        titulo = input("Digite o titulo do filme: ")
        resultado = buscar_filme_por_titulo(titulo)
        print(resultado)
    
    elif acao == 3:
        diretor = input("Digite o diretor: ")
        resultado = buscar_por_diretor(diretor)
        print(resultado)

    elif acao == 4:
        genero = input("Digite o gênero do filme: ")
        resultado = buscar_por_genero(genero)
        print(resultado)
        
    elif acao == 5:
        resultado = calcular_media_duracao()
        print(resultado)
    
    elif acao == 6:
        break

    else:
        print("Resposta invalida.")
