import Tree

# import sys
# sys.setrecursionlimit(3000) só um teste, pra adicionar mais limite de recursão no python na stack

t = Tree.Tree()

t.inserirV(*range(1, 20)) 
num: int = 0
cont = input("Digite se quer (insere, busca, nivel, somaRaizNo, inOrdem, sair): ")

while cont != "sair":
    
    if cont == "inOrdem":
        t.inOrdem()
    elif cont == "posOrdem":
        t.posOrdem()
    elif cont == "preOrdem":
        t.preOrdem()
    else:
        num = int(input("Digite o número: "))
        print(eval(f"t.{cont}({num})"))

    cont = input("Digite se quer (insere, busca, nivel, somaRaizNo, inOrdem, sair): ")
    