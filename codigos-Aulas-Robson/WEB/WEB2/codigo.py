import funcs

membros = {}

while True:
    print('Opções Menu do Clube: Adicionar Membro (1), Remover Membro (2), Listar Membros (3), Contar Quantidade de Membros (4), Fechar Programa (0)')
    opcao_menu = input('Digite a opção do menu: ')
    if opcao_menu == '0':
        break
    elif opcao_menu == '1':
        nome = input("Digite o Nome: ")
        idade = int(input("Digite a Idade: "))
        email = input("Digite o Email: ")
        cpf = input("Digite o CPF: ")
        funcs.adicionar_membro(nome, idade, email, cpf, membros)
    elif opcao_menu == '2':
        cpf_remover = input("Digite o CPF para Remover: ")
        funcs.remover_membro(cpf_remover, membros)
    elif opcao_menu == '3':
        lista_membros = {}
        lista_membros = funcs.listar_membros(membros)
        for cpf, nome in lista_membros.items():
            print(f'CPF: {cpf} | Nome: {lista_membros[cpf]['nome']} | Email: {lista_membros[cpf]['email']}')
    elif opcao_menu == '4':
        print(funcs.quantidade_membros(membros))