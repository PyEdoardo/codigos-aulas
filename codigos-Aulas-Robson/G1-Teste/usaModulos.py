import modulos

alunos = []

while True:
    nome = input("Digite o Nome do Aluno: ")
    if nome == '0':
        break

    notas = []

    for i in range(4):
        print('\n')
        nota = float(input("Digite a Nota: "))
        notas.append(nota)

    media = modulos.calcularMedia(notas)
    situacao = modulos.situacaoAluno(media)

    alunos.append([nome, notas, media, situacao])

