class No:
    def __init__(self, anterior, valor, proximo):
          self.ant = anterior
          self.info = valor
          self.prox = proximo
class Ldde:
    def __init__(self):
           self.prim = None
           self.ult = None
           self.quant = 0
           
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info}')
            aux = aux.prox

    def inserir_fim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1

    def remover_extremidades(self):
        if self.quant <= 2:
            self.prim = self.ult = None
            return
        self.prim = self.prim.prox
        self.prim.ant = None
        self.ult = self.ult.ant
        self.ult.prox = None
        self.quant -= 2
        
