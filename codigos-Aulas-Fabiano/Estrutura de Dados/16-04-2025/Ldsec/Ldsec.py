class No:
    def __init__(self, valor, prox):
          self.info = valor
          self.prox = prox
class Ldsec:
    def __init__(self):
          self.prim = None
          self.quant = 0

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info}')
            aux = aux.prox

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = No(valor, None)
            self.prim.prox = self.prim
        else:
            aux = self.prim
            while aux.prox != self.prim:
                aux = aux.prox
            aux.prox = No(valor, self.prim)
        self.quant += 1
        

    
