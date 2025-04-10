class No: #Este objeto guarda o um valor, um "ponteiro" para o próximo nó, e outro "ponteiro" para o nó anterior.
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Lddec:
    def __init__(self): #Construtor que deixa o "head/prim" e o "tail/ult" como None
        self.prim = self.ult = None
        self.quant = 0 #Esse quant basicamente regra a estrutura, fazendo o controle da quantidade de nós dentro da Lista
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.ult = self.prim = No(self.ult, valor, self.prim)
        else: 
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1
        
    def inserir_final(self, valor):
        if self.quant == 0:
            self.ult = self.prim = No(self.ult, valor, self.prim)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, self.prim)
            self.prim.ant = self.ult
        self.quant += 1  

    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult.prox = self.prim = self.prim.prox
            self.prim.ant = self.ult
        self.quant -= 1
        
    def remover_fim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim.ant = self.ult = self.ult.ant
            self.ult.prox = self.prim
        self.quant -= 1    

    def remover_val(self, valor):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            for i in range(self.quant):
                if aux.info == valor:
                    if self.quant == 1:
                        self.prim = None
                    else:
                        aux.ant.prox = aux.prox
                        aux.prox.ant = aux.ant
                        if aux == self.prim:
                            self.prim = aux.prox
                    self.quant -= 1
                    return
                aux = aux.prox


    def show(self):
        aux = self.prim
        
        #Teste
        prox = aux.prox
        ant = aux.ant
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Próximo: {prox.info} | Anterior: {ant.info}')
            aux = aux.prox
            prox = aux.prox
            ant = aux.ant
            
    def show_inverso(self):
        aux = self.ult
        
        #Teste
        prox = aux.prox
        ant = aux.ant
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Anterior: {prox.info} | Próximo: {ant.info}')
            aux = aux.ant
            prox = aux.prox
            ant = aux.ant
    
    def inserir_valores_final(self, *valores):
        if len(valores) <= 1:
            return
        for i in valores:
            self.inserir_final(i)
        
    def sort(self):
        if self.quant < 2:
            return
        valores = []
        aux = self.prim
        for i in range(self.quant):
            valores.append(aux.info)
            aux = aux.prox
        valores.sort()
        aux = self.prim
        for valor in valores:
            aux.info = valor
            aux = aux.prox
    
    def reverse(self):
        if self.quant < 2:
            return
        valores = []
        aux = self.prim
        for i in range(self.quant):
            valores.append(aux.info)
            aux = aux.prox
        aux = self.prim
        valores.sort(reverse=True)
        for valor in valores:
            aux.info = valor
            aux = aux.prox