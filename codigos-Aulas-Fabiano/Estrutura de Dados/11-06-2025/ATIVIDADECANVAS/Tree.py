'''
Implemente a função imprime_menores(self, valor) que
imprime em ordem crescente todos os valores menores que valor.

Implemente a função imprime_ancestrais(self, valor) que
imprime os valores de todos os nós que são ancestrais do nó que contém valor.

Implemente a função imprime_irmao(self, valor) que
imprime, se existir, o valor do nó irmão do nó que contém valor.

Implemente a função retorna_irmao(self, valor) que
retorna, se existir, o valor do nó irmão do nó que contém valor, ou None, caso não exista.

Implemente a função retorna_pai(self, valor) que
retorna, se existir, o valor do nó pai do nó que contém valor. Considere que o valor passado como argumento existirá na árvore.
'''

class Tree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def imprime_ancestrais(self, valor):
        if self.raiz == None:
            return
        else:
            return self.raiz.imprime_ancestrais(valor)
        

    def imprime_menores(self, valor):
        if self.raiz == None:
            return
        else:
            return self.raiz.imprime_menores(valor)

    def imprime_irmao(self, valor):
        if self.raiz == None:
            return
        else:
            return self.raiz.imprime_irmao(valor)
            
    def retorna_irmao(self, valor):
        if self.raiz == None:
            return
        else:
            return self.raiz.retorna_irmao(valor)


    def retorna_pai(self, valor):
        if self.raiz == None:
            return
        else:
            return self.raiz.retorna_pai(valor)


class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq is None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir is None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    
    def imprime_ancestrais(self, valor):
        if self.info == valor:
            return True
        
        elif valor < self.info:
            print(self.info)
            if self.esq != None:
                self.esq.imprime_ancestrais(valor)
            else:
                return False

        else:
            print(self.info)
            if self.dir != None: 
                self.dir.imprime_ancestrais(valor)
            else:
                return False

    def imprime_menores(self, valor):
        if self.info < valor:
            if self.esq != None:
                self.esq.imprime_menores(valor)
            print(self.info)
            if self.dir != None:
                self.dir.imprime_menores(valor)

        else:
            if self.esq != None:
                self.esq.imprime_menores(valor)

    def imprime_irmao(self, valor):
        #Unica forma que consegui é andar duas vezes na árvore, uma capturar o irmão e a outra pra printar o irmão
        noTemporario: No = None ##Sem usar esse typehint o meu vscode não mostra as funções
        if valor == self.info:
            return True
        
        elif valor < self.info:
            if self.esq != None:
                if self.esq.info == valor:
                    noTemporario = self.dir
                else:
                    return self.esq.imprime_irmao(valor)
        
        else:
            if self.dir != None:
                if self.dir.info == valor:
                    noTemporario = self.esq
                else:
                    return self.dir.imprime_irmao(valor)
        
        if noTemporario != None:
            return noTemporario.info
        else:
            return


    def retorna_irmao(self, valor):
        if valor == self.info:
            return self
        
        elif valor < self.info:
            if self.esq != None:
                if self.esq.info == valor:
                    if self.dir != None:
                        return self.dir.info
                else:
                    return self.esq.retorna_irmao(valor)

        else:
            if self.dir != None:
                if self.dir.info == valor:
                    if self.esq != None:
                        return self.esq.info
                else:
                    return self.dir.retorna_irmao(valor)
        
        return "Não encontrado"

    def retorna_pai(self, valor):
        if valor == self.info:
            return self.info

        elif valor < self.info:
            if self.esq != None:
                if self.esq.info == valor:
                    return self.info
                else:
                    return self.esq.retorna_pai(valor)

        else:
            if self.dir != None:
                if self.dir.info == valor:
                    return self.info
                else:
                    return self.dir.retorna_pai(valor)
        
        return "Não encontrado"




