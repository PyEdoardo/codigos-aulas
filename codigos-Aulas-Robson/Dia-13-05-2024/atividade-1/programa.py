import funcs

usuarios = {
 'edo' : {'nome' : 'Edoardo Tombolesi', 'ultimo_acesso' : '24/10/2023', 'id_maquina' : 'labin12'},
 'gab' : {'nome' : 'Gabriel', 'ultimo_acesso' : '24/10/2023', 'id_maquina' : 'labin34'}
}

while True:
    dados = input("Digite os Dados nesse formato: (login, nome, ultimo acesso, id_maquina) 0 para sair: ")
    if dados == '0':
        break
    login, nome, ultimo_acesso, id_maquina = dados.split(", ")
    if login not in usuarios:
        usuarios[login] = {'nome' : nome, 'ultimo_acesso' : ultimo_acesso, 'id_maquina' : id_maquina}
    else:
        print("Login já cadastrado!")

while True:
    opcao = int(input("Qual opção deseja? \n1: Listar todos os nomes de usuários\n2: Listar dados de um usuário\n3: Listar os nomes de usuários de uma data específica\n4: Alterar dados de um usuário\n5: Excluir um usuário\n6: Sair) "))
    
    if opcao == 6:
        break
    elif opcao == 1:
        for chave in usuarios:
            print(f'Nome: {usuarios[chave]["nome"]}')
    elif opcao == 2: 
        proc_user = input("Qual o Login a ser procurado: ")
        funcs.usuarios(proc_user, usuarios)
    elif opcao == 3:
        dataProc = input("Qual a data a ser pesquisada: ")
        print(f'{funcs.procData(dataProc, usuarios)}')
    elif opcao == 4:
        print("Opções: (todos, nome, último acesso ou id da máquina)\n")
        oqModificar = input("Qual opção: ")
        loginModificado = input("Qual o login que pretende modificar: ")
        if oqModificar == 'nome':
            novoNome = input("Digite o novo nome: ")
            print(f'Nome Antigo: {usuarios[loginModificado]["nome"]}, Novo Nome: {funcs.modificarNome(loginModificado, novoNome, usuarios)}')


