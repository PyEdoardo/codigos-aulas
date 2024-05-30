import funcoes

alunos = {

}
matricula = funcoes.criarMatricula('alunos.txt')

while True:
    matricula = funcoes.criarMatricula('alunos.txt')
    print("Opções: Cadastrar, Editar, Excluir, Imprimir Relatório, Sair: ")
    opcao = input("Digite a opção: ")
    if opcao in ['sair', 'Sair', 's', 'S']:
        break
    elif opcao in ['c', 'cadastro', 'cadastrar', 'cad']:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        g1 = float(input("G1: "))
        g2 = float(input("g2: "))
        carga_horaria = int(input("Digite a porcentagem de carga horária: "))
        status_aluno = None
        funcoes.cadastroAluno(alunos, 1, nome, idade, g1, g2, carga_horaria, status_aluno, 'alunos.txt')
    elif opcao in ['e', 'editar', 'edit', 'edito']:
        print("Opções: Nome, Idade, G1, G2, Carga Horária, Status Aluno ou Tudo")
        sub_menu = input("Oque Deseja Alterar?: ")
        qual_usuario = int(input("Digite a matrícula do usuário para modificar: "))
        if sub_menu.lower() in ['nome', 'n', 'name']:
            novo_nome = input("Digite o novo nome: ")
            alunos[qual_usuario]['nome'] = novo_nome
        elif sub_menu.lower() in ['idade', 'id']:
            nova_idade = int(input("Digite a nova idade: "))
            alunos[qual_usuario]['idade'] = nova_idade
        elif sub_menu.lower() in ['g1']:
            nova_g1 = float(input("Digite a nota de G1: "))
            alunos[qual_usuario]['g1'] = nova_g1
        elif sub_menu.lower() in ['g2']:
            nova_g2 = float(input("Digite a nota de G2"))
            alunos[qual_usuario]['g2'] = nova_g2
        elif sub_menu.lower() in ['carga horaria', 'carga horária', 'carga', 'c', 'horas', 'horária', 'hora']:
            nova_carga_horaria = float(input("Digite a carga horária em porcentagem: "))
            alunos[qual_usuario]['carga_horaria'] = nova_carga_horaria
        elif sub_menu.lower() in ['status', 'situação', 'situacao', 'sit', 's']:
            novo_status = input("Digite o novo status: ")
            alunos[qual_usuario]['status'] = novo_status
        elif sub_menu.lower() in ['tudo', 'todos', 't']:
            novo_nome = input("Digite o novo nome: ")
            alunos[qual_usuario]['nome'] = novo_nome
            nova_idade = int(input("Digite a nova idade: "))
            alunos[qual_usuario]['idade'] = nova_idade
            nova_g1 = float(input("Digite a nota de G1: "))
            alunos[qual_usuario]['g1'] = nova_g1
            nova_g2 = float(input("Digite a nota de G2"))
            alunos[qual_usuario]['g2'] = nova_g2
            nova_carga_horaria = float(input("Digite a carga horária em porcentagem: "))
            alunos[qual_usuario]['carga_horaria'] = nova_carga_horaria
            novo_status = input("Digite o novo status: ")
            alunos[qual_usuario]['status'] = novo_status
        else:
            print("Opção Errada!!\n")
    

            



        
