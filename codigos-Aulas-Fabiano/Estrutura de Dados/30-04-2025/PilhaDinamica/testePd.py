import Pd

pilha = Pd.Pd()

pilha.push("A")
print(pilha.ver_topo())
pilha.push("B")
print(pilha.ver_topo())
pilha.push("C")
print(pilha.ver_topo())
pilha.pop()
print(pilha.ver_topo())