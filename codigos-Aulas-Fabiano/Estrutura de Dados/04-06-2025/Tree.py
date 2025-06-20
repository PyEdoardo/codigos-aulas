class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)
        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def mostrar_caminho(self, valor): ##mostra caminho até o valor
        print(self.info)
        if self.info == valor:
            return
        elif valor < self.info and self.esq != None:
            self.esq.mostrar_caminho(valor)
        elif valor > self.info and self.dir != None
            self.dir.mostrar_caminho(valor)

    def conta_quantos(self, valor): #quantas vezes tem um valor repetido
        cont = 0
        if self.info == valor:
            cont = 1
        
        if self.esq != None:
            cont += self.esq.conta_quantos(valor)
        if self.dir != None:
            cont += self.dir.conta_quantos(valor)
        
        return cont
    
    def maior_filho(self, valor):
    # Busca o nó com o valor
        if self.info == valor:
            maior = None
            if self.esq and self.dir:
                maior = max(self.esq.info, self.dir.info)
            elif self.esq:
                maior = self.esq.info
            elif self.dir:
                maior = self.dir.info
            return maior
        
        elif valor < self.info and self.esq != None:
            return self.esq.maior_filho(valor)
        elif valor > self.info and self.dir != None:
            return self.dir.maior_filho(valor)

    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
            
    #Retorna o nível do valor procurado
    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.nivel(valor) + 1
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.nivel(valor) + 1
    
    def somaRaizNo(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.nivel(valor) + self.info
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.nivel(valor) + self.info
    
    def inOrdem(self):
        if self.esq != None:
            self.esq.inOrdem()
        print(self.info, end=" ")
        if self.dir != None:
            self.dir.inOrdem()
    
    def preOrdem(self):
        pass

    def posOrdem(self):
        pass


class Tree:
    # Pré-ordem: o pai é visitado antes dos filhos, ou seja, Pai-Esquerda-Direita;
    # Em ordem: o pai é visitado entre os filhos, ou seja, Esquerda-Pai-Direita;
    # Pós-ordem: o pai é visitado após os filhos, ou seja, Esquerda-Direita-Pai;

    def __init__(self):
        self.raiz: No = None

    def inserirV(self, *valores):
        for i in valores:
            self.insere(i)

    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            self.raiz.insere(valor)

    def busca(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.busca(valor)
    
    #Retorna o nível
    def nivel(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.nivel(valor) - 1
    
    def somaRaizNo(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.somaRaizNo(valor) - 1
        
    def inOrdem(self):
        if self.raiz != None:
            self.raiz.inOrdem()

    def preOrdem(self):
        if self.raiz != None:
            self.raiz.preOrdem()

    def posOrdem(self):
        if self.raiz != None:
            self.raiz.posOrdem()