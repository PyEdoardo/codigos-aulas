import Pd

def calcular_expressao(expressao):
    pilha = Pd.Pd()
    operadores = {'+', '-', '*', '/'}
    tokens = expressao.split()

    for token in tokens:
        if token not in operadores:
            pilha.push(float(token))
        else:
            b = pilha.ver_topop()
            a = pilha.ver_topop()
            if a is None or b is None:
                raise ValueError("Expressão inválda, a ou b nulos") #O Raise é igual a um throw no java.
            resultado = eval(f'{a}{token}{b}')
            pilha.push(resultado)
    return pilha.ver_topo()
        
calculo = input("Digite a expressão em notação polonesa reversa: ")
print(f'O resultado é: {calcular_expressao(calculo)}')
