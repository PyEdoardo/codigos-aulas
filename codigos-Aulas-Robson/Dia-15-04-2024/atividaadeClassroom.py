import modulos_atv

nome_func = input("Digite o Nome do Funcionário: ")
salario = float(input("Digite o Salário do Funcionário: "))

while nome_func != '0':
    indice = 0
    funcionarios = []
    funcionarios[indice].append(nome_func)
    salarios = []
    salarios[indice].append(salario)
    abonos = []
    abonos[indice].append(modulos_atv.abono(salario))
    nome_func = input("Digite o Nome do Funcionário: ")
    salario = float(input("Digite o Salário do Funcionário: "))
    indice =+ 1

while True:
    i = 0
    print(f'Projeção de Gastos com Abono: ')
    print(f'\nColaborador  |  Salário  |  Abono')
    print(f'{funcionarios[i]}  |  {salarios[i]}  |  {abonos[i]}\n')
    print(f'Total: {modulos_atv.total_salario(salarios)}, {modulos_atv.total_Abonos(abonos)}')
    print(f'Maior Abono Pago: {modulos_atv.maior_Abono(abonos)}')
    print(f'Média de Abono Salarial: {modulos_atv.mediaAbono(abonos)}')
    print(f'Foram Pagos Abonos Abáixo da Média a {modulos_atv.menoresAbonos} colaboradores')


