import modulos

alunos = []

while True:
    nome = input("Digite o Nome do Aluno: ")
    if nome == '0':
        break

    notas = []

    for i in range(4):
        nota = float(input("Digite a Nota: "))
        notas.append(nota)

    media = modulos.calcularMedia(notas)
    situacao = modulos.situacaoAluno(media)

    alunos.append([nome, notas, media, situacao])

i = 0
qtAprovados = 0
qtReprovados = 0

while i < len(alunos):
    if alunos[i][3] == 'Aprovado':
        qtAprovados = qtAprovados + 1
    elif alunos[i][3] == 'Reprovado':
        qtReprovados = qtReprovados + 1
    i = i + 1    

i = 0
print("\nEscola Primavera - Gestão de Alunos\n-----------------------------------------------------")
while i < len(alunos):
    print(f'Nome: {alunos[i][0]} | Notas: {alunos[i][1]}')
    print(f'Média: {alunos[i][2]} | Situação: {alunos[i][3]}')
    print('-----------------------')
    
    
    i = i + 1
print(f'\nForam Processados {len(alunos)} alunos')
print(f'Total de Alunos Aprovados: {qtAprovados}')
print(f'Total de Alunos Reprovados: {qtReprovados}')
print(f'Maior Media: {modulos.maiorMedia(alunos)}')
print(f'Menor Media: {modulos.menorMedia(alunos)}')
print(f'Dois Primeiros Alunos: {modulos.doisPrimeiros(alunos)}')
print(f'Dois Ùltimos Alunos: {modulos.doisUltimos(alunos)}')
i = 0
while i < len(alunos):
    print(alunos[i][0].sorted())
    i = i + 1
