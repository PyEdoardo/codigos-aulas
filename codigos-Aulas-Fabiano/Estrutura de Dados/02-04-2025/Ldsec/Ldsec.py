class No: 
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Ldsec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.prim = self.ult.prox = No(valor, self.prim)
        self.quant += 1

    def inserir_final(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
            self.prim.prox = self.prim
        else:
            self.ult.prox = self.ult = No(valor, self.prim)
        self.quant += 1

    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.ult.prox = self.prim.prox
        self.quant -= 1
    
    def remover_fim(self):
        aux = self.prim
        for i in range(self.quant):
            if aux.prox != self.ult:
                aux = aux.prox
            else:
                self.ult = aux
                self.ult.prox = self.prim
        self.quant -= 1


    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info}')
            aux = aux.prox
    
    def remover_val(self, valor):
        aux = self.prim
        ant = None
        for i in range(self.quant):
            if aux.info == valor:
                if aux == self.prim:
                    if self.quant == 1:
                        self.prim == None
                    else:
                        ult = self.prim
                        while ult.prox != self.prim:
                            ult = ult.prox
                        self.prim = aux.prox
                        ult.prox = self.prim
                else:
                    ant.prox = aux.prox
                self.quant -= 1
                return
            aux = aux.prox
    
            