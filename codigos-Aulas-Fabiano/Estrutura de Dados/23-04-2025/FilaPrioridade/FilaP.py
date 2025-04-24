import FilaD

class FilaP:

    def __init__(self):
        self.f1 = FilaD.FilaD()
        self.f2 = FilaD.FilaD()
        self.f3 = FilaD.FilaD()
    
    def inserir(self, valor, prior):
        if prior == 1:
            self.f1.inserir(valor)
        elif prior == 2:
            self.f2.inserir(valor)
        else:
            self.f3.inserir(valor)
    
    def remover(self): #1, 2 ,3
        if not self.f1.esta_vazio():
            self.f1.remover()
            return
        elif not self.f2.esta_vazio():
            self.f2.remover()
            return
        elif not self.f3.esta_vazio():
            self.f3.remover()
            return
        else:
            print("Listas vazias!")
    
    def ver_prim(self):
        if not self.f1.esta_vazio():
            return self.f1.ver_primeiro()
        elif not self.f2.esta_vazio():
            return self.f2.ver_primeiro()
        elif not self.f3.esta_vazio():
            return self.f3.ver_primeiro()        
        else:
            return "Listas Vazias!"


    