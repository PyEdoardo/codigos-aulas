import funcs

arquivojson = 'alunos.json'
arquivotexto = 'situacao.txt'
while True:
    print("Opções: Situação Alunos (1), Alterar Notas (2), Exportar Situação (3), Fechar Programa (0)\n")
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
        print(funcs.alterarNotas(matriculaAlterar, nota1Nova, nota2Nova, arquivojson))
    elif menu == 3:
        funcs.exportarSituacao(funcs.situacaoAlunos(arquivojson), arquivotexto)
        

