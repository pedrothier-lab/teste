cinema = []
numero_lugares = 0
for i in range(5):
  fileira = []
  for i in range(10):
    fileira.append("L")
  cinema.append(fileira)

print(f"{4 * "- " }CINEMA ATUAL {4 * "- " }\nNúmero de lugares ocupados: {numero_lugares}\nNúmero de lugares disponíveis: {50 - numero_lugares}\n")
for i in cinema:
  print (i)

while numero_lugares < 50:

  fileira_escolhida = int(input("\nNúmero da fileira (0-4): "))
  coluna_escolhida = int(input("Número da coluna (0-9): "))

  if fileira_escolhida < 0 or fileira_escolhida > 4 or coluna_escolhida < 0 or coluna_escolhida > 9:
    print("Lugar inválido. Escolha uma fileira de 0 a 4 e a coluna de 0 a 9.")
    continue

  if cinema[fileira_escolhida][coluna_escolhida] == "O":
    print("Ja existe uma pessoa ocupando este lugar.")
    continue

  cinema[fileira_escolhida][coluna_escolhida] = "O"
  print(f"\n{4 * "- " }CINEMA DEPOIS {4 * "- " }\n")
  numero_lugares = numero_lugares +1

  for i in cinema:
    print(i)
  print(f"\nNúmero de lugares ocupados: {numero_lugares}\nNúmero de lugares disponíveis: {50 - numero_lugares}\n")

  continuar = str(input("Deseja continuar? (sim/nao) "))
  if continuar == "sim":
    continue
  else:
    break
