clientes = [] #lista aninhada vazia dos clientes

continuar = input("Deseja inserir dados na copiadora? (s ou n): ") #flag pra continuar ou parar o codigo.
while continuar != 'n': #enquanto o continuar for diferente de 'n' que seria o não, ele fica preso nesse loop.
    cod_cli = input("Digite o Código do Cliente: ") #numero do código do cliente.
    print("\nTipos de Usuário: (professor, aluno, ou qualquer outro) ") #aqui mostra os tipos de usuário, sendo eles professor, aluno ou outro qualquer
    tipo_user = input("Digite o Tipo de Usuário: ")
    qt_copia = int(input("Digite a quantidade de cópias: "))
    clientes.append([cod_cli, tipo_user, qt_copia, 0]) #me adiantei e coloquei o valor a pagar como sendo 0 na criação da lista, assim deixa o resto do código minimalista
    continuar = input("Deseja inserir mais dados na copiadora? (s ou n): ")
valor_pagar = 0 #variavel pra guardar o valor a pagar do cliente

i = 0 
while i < len(clientes):
    if clientes[i][1] == 'professor':
        if clientes[i][2] > 50: #se a quantidade de cópias for maior que 50 tem 10 pag de desconto
            clientes[i][2] = clientes[i][2] - 10
            valor_pagar = clientes[i][2] * 0.08
        else:
            valor_pagar = clientes[i][2] * 0.08
    elif clientes[i][1] == 'aluno':
        valor_pagar = clientes[i][2] * 0.10
    else:
        valor_pagar = clientes[i][2] * 0.15               
    clientes[i][3] = valor_pagar
    i = i + 1        

i = 0
while i < len(clientes):
    print('-------------------------------------------------------------------------------------------')#barras pra separar do conteúdo de cima do cmd
    print(f'\nCódigo Usuário: {clientes[i][0]} \nValor a Pagar: R${clientes[i][3]} ') #print que sai os valores a pagar de cada usuário
    print('-------------------------------------------------------------------------------------------') #algumas barras pra separar e deixar o código mais legível
    i = i + 1


   

