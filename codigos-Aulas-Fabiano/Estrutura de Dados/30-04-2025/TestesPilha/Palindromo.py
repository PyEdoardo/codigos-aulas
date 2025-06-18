import Pd


def e_palindromo(palavra: str) -> bool:
    pilha = Pd.Pd()
    for letra in palavra.lower():
        pilha.push(letra)
    for letra in palavra.lower():
        topo = pilha.ver_topop()
        print(f"Comparando {letra} com {topo}")
        if topo != letra:
            return False
    return True

teste = input("Digite uma palavra (não digite em maiúsculo!): ")
print(f'É palindromo' if e_palindromo(teste) else "Não é palíndromo")

