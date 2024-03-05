import funcoes

while True:
    print("\n1Seja bem-vindo ao programa usaFuncoes.py. Por favor, escolha a opção desejada: \n1 – Verifica número inteiro e retorna True ou False\n2 – Verifica se um número é positivo ou negativo\n3 – Verifica se um número é ímpar ou par\n4 - Realiza o cáluclo de médias ponderadas ou aritméticas\n5 - Transforma a idade informada em Dias\n6 - Ordena uma lista de 3 número\n7 - Tranforme Segundos em Horas, Minutos e Segundos\n8 - Verifique se um número é perfeito ou não\n9 - Calcula o Peso com base no sexo e altura\n10 - Recebe 3 Valores Reais e Verifica os Lados de um Triangulo\n0 - Sair\n")
    opcaoMenu = input("Digite Qual Opção a Desejada: ")
    if opcaoMenu == '1':

        numero = float(input("Digite um Número: "))
        print(funcoes.numVerdFalso(numero))

    elif opcaoMenu == '2':

        numero = float(input("Digite um Número: "))
        print(funcoes.numVerdFalso2(numero))

    elif opcaoMenu == '3':

        numero = float(input("Digite um Número: "))
        print(funcoes.valorImparPar(numero))

    elif opcaoMenu == '4':

        tipoAluno = input("Deseja Qual Tipo de Média?\nDigite 'A' para Média Aritmética\nOu Digite 'P' para Média Ponderada: ")
        n1 = float(input("Qual Foi a 1° Nota?"))
        n2 = float(input("Qual Foi a 2° Nota?"))
        n3 = float(input("Qual Foi a 3° Nota?"))

        print(f'\nTotal das Notas: \nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\nTipo de Média: {tipoAluno}\nMédia: {funcoes.mediasAluno(n1, n2, n3, tipoAluno)}')

    elif opcaoMenu == '5':

        qtAnos = int(input("Digite a Quantidade de Anos: "))

        qtMeses = int(input("Digite a Quantidade de Meses: "))

        qtDias = int(input("Digite a Quantidade de Dias: "))

        print(f'Quantidade de Dias: {funcoes.idadeEmDias(qtAnos, qtMeses, qtDias)}')

    elif opcaoMenu == '6':
        
        num1 = int(input("Digite o 1 Inteiro:\n "))
        num2 = int(input("Digite o 2 Inteiro:\n "))
        num3 = int(input("Digite o 3 Inteiro:\n "))

        print(funcoes.ordenarNumeros(num1, num2, num3))

    elif opcaoMenu == '7':

        seg = int(input('Digite uma hora em segundos: '))
        print(funcoes.horas(seg))

    elif opcaoMenu == '8':

        num = int(input('Digite um numero para saber se e perfeito ou não: '))
        print(f'{num} e numero perfeito? {funcoes.numero(num)} ')

    elif opcaoMenu == '9':

        alt = float(input('Digite sua altura: '))
        sex = input('Seu sexo: ')
        print(funcoes.pesoIdeal(alt, sex))

    elif opcaoMenu == '10':

        dadosA = float(input('Digite o valor do ladoA: '))
        dadosB = float(input('Digite o valor do ladoB: '))
        dadosC = float(input('Digite o valor do ladoC: '))

        print(funcoes.triangulo(dadosA, dadosB, dadosC))

    elif opcaoMenu == '0':
        break