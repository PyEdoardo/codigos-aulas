class No:
    def __init__(self, valor):
        self.info = valor
        self.esq = None
        self.dir = None

class Abb:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)
    
    def _inserir(self, atual: No, valor):
        if valor < atual.info:
            if atual.esq is None:
                atual.esq = No(valor)
            else:
                self._inserir(atual.esq, valor)
        else:
            if atual.dir is None:
                atual.dir = No(valor)
            else:
                self._inserir(atual.dir, valor)
    
    def inserirV(self, *args):
        for valor in args:
            self.inserir(valor)

    def show(self):
        self._show(self.raiz)

    def _show(self, no: No):
        if no is not None:
            self._show(no.esq)
            print(f'Valor: {no.info}')
            self._show(no.dir)
    
    def mostrar_grafico(self):
        self._mostrar_grafico(self.raiz, 0)

    def _mostrar_grafico(self, no: No, nivel):
        if no is not None:
            self._mostrar_grafico(no.dir, nivel + 1)
            print(f'   ' * nivel + f'-> {no.info}')
            self._mostrar_grafico(no.esq, nivel + 1)