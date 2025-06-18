import Pd

expressao = input("Digite a expressão: ")

def e_valido(expressao: str) -> bool:
    pilha = Pd.Pd()
    for i in expressao:
        match i:
            case '(':
                pilha.push(i)
            case ')':
                if pilha.esta_vazia():
                    return False
                pilha.pop()
    return pilha.esta_vazia()

print(e_valido(expressao))