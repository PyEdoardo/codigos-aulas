class No:
    def __init__(self,valor,proximo):
        self.info = valor
        self.prox = proximo
class Ldse:
    def __init__(self):
        self.prim = None
        self.quant = 0
    def inserir_inicio(self,valor):
        self.prim = No(valor,self.prim)
        self.quant += 1
    def remover_fim(self):
        if self.prim is None:
            return
        if self.prim.prox is None:
            self.prim = None
        else:
            aux = self.prim
            while aux.prox.prox is not None:
                aux = aux.prox
            aux.prox = None
        self.quant -= 1
    def remover_inicio(self):
        self.prim = self.prim.prox
        self.quant -= 1
    def remover_fim(self):
        if self.quant == 0:
            self.prim = No(valor,None)
        else:
            aux = self.prim
            while aux.prox != None:
                aux = aux.prox
                aux.prox = No(valor,None)
        self.quant += 1
    def show(self):
        aux = self.prim
        while aux!=None:
            print(aux.info, end=' ')
            aux = aux.prox
        print()
