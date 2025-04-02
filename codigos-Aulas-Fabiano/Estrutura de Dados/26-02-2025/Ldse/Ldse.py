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
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def inserir_final(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = No(valor, None)
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    # def remover_final(self): se recusa a funcionar, o debaixo funciona normalmente
    #     if self.quant == 1:
    #         self.prim = self.ult = None
    #     else:
    #         aux = self.prim
    #         while aux.prox is not self.ult:
    #             aux = aux.prox
    #         self.ult = aux
    #         aux.prox = None
    #     self.quant -= 1

    def remover_final(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            for i in range(self.quant - 2):
                aux = aux.prox
            self.ult = aux
            aux.prox = None
        self.quant -= 1

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.prox