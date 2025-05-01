import Pd

pilha1 = Pd.Pd()

expressao: str = input("Digite a expressão: ")

for i in expressao:
    match i:
        case "(": pilha1.push("(")
        case ")":
            if pilha1.esta_vazia():
                print("Não é válido!")
                break