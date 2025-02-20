import les

l1 = les.Les(5)
l2 = les.Les(4)

if not l1.esta_cheia():
    l1.inserir_fim('A')
if not l1.esta_cheia():
    l1.inserir_inicio('B')
if not l1.esta_cheia():
    l1.inserir_fim('C')
if not l1.esta_cheia():
    l1.inserir_inicio('D')
if not l1.esta_cheia():
    l1.inserir_fim('E')
print("Antes de inserir F")
print("Esperado: DBACE")

if not l1.esta_cheia():
    l1.inserir_fim('F')
print("Após inserir F")
print("Esperado: DBACE")
l1.show()
for i in range(2):
    l2.inserir_fim(l1.get_quant())
    l1.remover_inicio()
print("l1 após o for")
print("Esperado: ACE")
l1.show()
print("l2 após o for")
print("Esperando: DB")
l2.show()

print("l1 antes de inserir G após A")
print("Esperando: ACE")
l1.show()
print("l1 depois de inserir G após A")
print("Esperando AGCE")
l1.inserir_apos("G", "A")
l1.show()
print("l1 depois de inserir H após E")
l1.inserir_apos("H", "E")
l1.show()
print('l1 após remover inicio')
print('Esperando GCEH')
l1.remover_inicio()
l1.show()

print("f1 após remover fim")
print("Esperando: GCE")
l1.remover_fim()
l1.show()
print("l1 depois de inserir I após H")
print("Esperando: GCE")
l1.inserir_apos("I", "H")
l1.show()
print("l2 antes de inserir K antes de D")
print("Esperando DB")
l2.show()

print("l2 depois de inserir K antes de D")
print("Esperado: KDB")
l2.inserir_antes("L", "D")
l2.show()
if l1.get_quant() > l2.get_quant():
    print("l1 é maior que l2")
elif i.get_quant() < l2.get_quant():
    print("l2 é maior que l1")
else:
    print("As duas tem o mesmo tamanho")

