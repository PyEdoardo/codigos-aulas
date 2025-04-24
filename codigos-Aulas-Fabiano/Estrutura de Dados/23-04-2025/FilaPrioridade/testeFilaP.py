import FilaP

filaP = FilaP.FilaP()
filaP.inserir('V1', 1)
filaP.inserir('V2', 1)
filaP.inserir('C1', 2)
filaP.inserir('G1', 3)

print(filaP.ver_prim())

filaP.remover()

print(filaP.ver_prim())
