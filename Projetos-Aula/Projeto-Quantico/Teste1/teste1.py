# Importar os módulos necessários do Qiskit
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# Criar um circuito quântico com um qubit
circuit = QuantumCircuit(1, 1)

# Aplicar uma porta Hadamard ao qubit
circuit.h(0)

# Medir o qubit
circuit.measure(0, 0)

# Visualizar o circuito
print("Circuit:")
print(circuit.draw())

# Escolher o simulador Aer qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

# Compilar e executar o circuito no simulador
compiled_circuit = transpile(circuit, simulator)
qobj = assemble(compiled_circuit)
result = simulator.run(qobj).result()

# Obter e imprimir os resultados da execução
counts = result.get_counts()
print("Result:")
print(counts)

# Opcional: Visualizar o histograma dos resultados
plot_histogram(counts).show()
