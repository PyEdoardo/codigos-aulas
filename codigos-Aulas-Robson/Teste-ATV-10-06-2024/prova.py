import funcs

arquivojson = 'alunos.json'
arquivotexto = 'situacao.txt'
while True:
    print("Opções: Situação Alunos (1), Alterar Notas (2), Exportar Situação (3), Adicionar Aluno (4), Fechar Programa (0)\n")
    menu = int(input("Qual será a sua opção: "))
    if menu == 0:
        break
    elif menu == 1:
        situacao = funcs.situacaoAlunos(arquivojson)
        for aluno in situacao:
            print(f'Matrícula: {situacao[aluno]["matricula"]}, Nome: {situacao[aluno]["nome"]}, Situação: {situacao[aluno]["situacao"]}')
    elif menu == 2:
        matriculaAlterar = input("Qual matrícula gostaria de alterar: ")
        nota1Nova = float(input("Digite a nova nota1: "))
        nota2Nova = float(input("Digite a nova nota2: "))
        frequenciaNova = float(input("Digite a nova Frequência: "))
        print(funcs.alterarSituacao(matriculaAlterar, nota1Nova, nota2Nova, frequenciaNova, arquivojson))
    elif menu == 3:
        funcs.exportarSituacao(funcs.situacaoAlunos(arquivojson), arquivotexto)
    elif menu == 4:
        nome = input("Qual o nome do Aluno: ")
        nota1 = float(input("Digite a nota1 do Aluno: "))
        nota2 = float(input("Digite a nota2 do Aluno: "))
        frequencia = float(input("Digite a Frequência do Aluno: "))
        funcs.adicionarAluno(nome, nota1, nota2, frequencia, arquivojson)
        

