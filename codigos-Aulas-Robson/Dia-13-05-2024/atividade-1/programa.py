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
    opcao = int(input("Qual opção deseja? \n1: Listar todos os nomes de usuários\n2: Listar dados de um usuário\n3: Listar os nomes de usuários de uma data específica\n4: Alterar dados de um usuário\n5: Excluir um usuário\n6: Sair\nDeseja qual opção:  "))
    
    if opcao == 6:
        break
    elif opcao == 1:
        for chave in usuarios:
            print(f'Nome: {usuarios[chave]["nome"]}')
    elif opcao == 2: 
        proc_user = input("Qual o Login a ser procurado: ")
        print(f'{funcs.procLogin(proc_user, usuarios)}')
    elif opcao == 3:
        dataProc = input("Qual a data a ser pesquisada: ")
        print(f'{funcs.procData(dataProc, usuarios)}')
    elif opcao == 4:
        print("Opções: (todos, nome, último acesso ou id da máquina)\n")
        oqModificar = input("Qual opção: ")
        loginModificado = input("Qual o login que pretende modificar: ")
        if oqModificar == 'nome':
            novoNome = input("Digite o novo nome: ")
            print(f'Nome Antigo: {usuarios[loginModificado]['nome']} | Nome Novo: {novoNome}')
            funcs.modificarNome(loginModificado, novoNome, usuarios)
        elif oqModificar == 'ultimo' or oqModificar == 'ultimo acesso' or oqModificar == 'último acesso':
            novoAcesso = input("Qual seria a nova data: ")
            print(f'Data Antiga: {usuarios[loginModificado]['ultimo_acesso']} | Nova Data: {novoAcesso}')
            funcs.modificarData(login=loginModificado, novaData=novoAcesso, usuarios=usuarios)
        elif oqModificar == 'id' or oqModificar == 'id maquina' or oqModificar == 'id da maquina':
            novoId = input("Digite o Novo ID: ")
            print(f'ID Antigo: {usuarios[loginModificado]['id_maquina']} | Novo ID: {novoId}')
            funcs.modificarID(loginModificado, novoId, usuarios)
        elif oqModificar == 'todos' or oqModificar == 'tudo' or oqModificar == 'todo':
            novoNome = input("Digite o novo nome: ")
            novoAcesso = input("Qual seria a nova data: ")
            novoId = input("Digite o Novo ID: ")
            listaNovos = [novoNome, novoAcesso, novoId]
            print(f'Nome Antigo: {usuarios[loginModificado]['nome']} | Nome Novo: {novoNome}\nData Antiga: {usuarios[loginModificado]['ultimo_acesso']} | Nova Data: {novoAcesso}\nID Antigo: {usuarios[loginModificado]['id_maquina']} | ID Novo: {id_maquina}')
            