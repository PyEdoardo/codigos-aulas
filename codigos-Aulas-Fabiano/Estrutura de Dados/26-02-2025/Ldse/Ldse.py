class No:
    
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldse:

    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        
