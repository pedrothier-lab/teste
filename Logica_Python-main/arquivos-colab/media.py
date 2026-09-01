alunos = {}
for i in range(3):
  nome = input(f"Qual o nome do {i+1}° aluno? ")
  nota = float(input(f"Qual a nonta de {nome}? "))
  alunos[nome] = nota

soma = 0

for nome,nota in alunos.items():
  print(f"Aluno: {nome} - Nota: {nota}")
  soma = soma + nota

media = soma / len(alunos)
print(f"A média é {media:.2f}")