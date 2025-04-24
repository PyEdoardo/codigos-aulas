class No:
    
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Fd:

    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def inserirV(self, *valores):
        for i in valores:
            self.inserir(i)
    
    def remover(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def ver_primeiro(self):
        return self.prim.info

    def esta_vazio(self):
        return self.prim == 0

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.prox