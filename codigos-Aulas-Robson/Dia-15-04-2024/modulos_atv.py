## (A)
def salarioTotal(salario):
    abono = salario * 0.25
    if abono < 200:
        abono = 200
    salario_total = abono + salario
    return salario_total

def abono(salario):
    abono = salario * 0.25
    if abono < 200:
        abono = 200
    return abono    
## (B)
def total_Colaboradores(funcionarios):
    totalFunc = 0
    for i in funcionarios:
        totalFunc = totalFunc + 1
    return totalFunc

## (C)
def total_salario(salarios):
    totalDeSalarios = 0
    indice = 0
    for i in salarios:
        totalDeSalarios = salarios[indice]
        indice = indice + 1
    return totalDeSalarios

## (D)

def total_Abonos(abonos):
    totalAbono = 0
    indice = 0
    for i in abonos:
        totalAbono = abonos[indice]
        indice = indice + 1
    return totalAbono

## (E)
# não consegui fazer a E
## (F)
def maior_Abono(abonos):
    maiorAbono = 0
    i = 0
    while maiorAbono < abonos[i]:
        if maior_Abono > abonos[i]:
            maior_Abono = abonos[i]
        i = i + 1
    return maiorAbono    
## (G)
def mediaAbono(abonos):
    mdiaAbono = 0
    totalAbono = 0
    indice = 0
    for i in abonos:
        totalAbono = abonos[i]
        indice = indice + 1
    mdiaAbono = totalAbono / indice
    return mdiaAbono    
## (H)

def menoresAbonos(abonos, mediaAbono):
    i = 0
    qt_menores = 0
    for i in abonos:
        if abonos[i] < mediaAbono:
            qt_menores = qt_menores + 1
    return qt_menores


    
        

            
