tabuleiro = [[" " for _ in range(3)] for _ in range(3)] 
jogadas = 0 

def mostrar_tabuleiro(): 
    print("\n Tabuleiro:\n") 
    print("   0   1   2") 
    for i in range(3): 
        print(f"{i}  " + " | ".join(tabuleiro[i])) 
        if i < 2: 
            print("   " + "---" * 3) 
    print() 

def verificar_vencedor(): 
    for i in range(3): 
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ": 
            return True 
    for j in range(3): 
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ": 
            return True 
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ": 
        return True 
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ": 
        return True 
    return False 

mostrar_tabuleiro() 

while jogadas < 9: 

    while True: 
        print("Vez do jogador X") 
        fileira_x = int(input("Digite a fileira/linha (0-2): ")) 
        coluna_x = int(input("Digite a coluna (0-2): ")) 
        
        if not (0 <= fileira_x <= 2 and 0 <= coluna_x <= 2): 
            print("Escolha números de 0 a 2.\n") 
            continue 
        if tabuleiro[fileira_x][coluna_x] == " ": 
            tabuleiro[fileira_x][coluna_x] = "X" 
            jogadas += 1 
            break 
        else: 
            print("Posição ocupada, tente de novo.\n") 
            
    mostrar_tabuleiro() 
    if verificar_vencedor(): 
        print("Parabéns, o jogador X venceu o jogo!") 
        break 
    if jogadas == 9: 
        break 

    while True: 
        print("Vez do jogador O") 
        fileira_o = int(input("Digite a fileira/linha (0-2): ")) 
        coluna_o = int(input("Digite a coluna (0-2): ")) 
        
        if not (0 <= fileira_o <= 2 and 0 <= coluna_o <= 2): 
            print("Escolha números de 0 a 2.\n") 
            continue 
        if tabuleiro[fileira_o][coluna_o] == " ": 
            tabuleiro[fileira_o][coluna_o] = "O" 
            jogadas += 1 
            break 
        else: 
            print("Posição ocupada, tente de novo.\n") 
            
    mostrar_tabuleiro() 
    if verificar_vencedor(): 
        print("Parabéns, o jogador O venceu o jogo!!") 
        break 

if not verificar_vencedor() and jogadas == 9: 
    print("Deu velha!")
