import funcoes

alunos = {}
notasString = funcoes.lerNotas("notas.txt")

for aluno in notasString[1:]:
    matricula, nome, g1, g2 = aluno.split(",")
    mp = (float(g1) + (float(g2) * 2)) / 3
    alunos[matricula] = {"nome" : nome, "g1" : g1, "g2" : g2, "mp" : round(mp, 1)}

print(alunos)

funcoes.salvarMP('mp.txt', alunos)