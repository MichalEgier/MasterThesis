import numpy as np
from qiskit import QuantumCircuit, transpile
#from qiskit.providers.aer import QasmSimulator     - tak bylo w poradniku ale tego nie widzi przy imporcie
from qiskit.visualization import plot_histogram
#added
from qiskit import Aer
import matplotlib.pyplot as plt

# backends - those here are used as simulators only (not for actual quantum devices)
# Use Aer's qasm_simulator
simulator = Aer.get_backend("qasm_simulator") #simulator for running the circuits (with measuring the qubits) (no noise - to check) (is it for real devices?)
#simulator = Aer.get_backend("aer_simulator") #simulator with automatic selection of further strategy (statevector, density_matrix, stabilizer, ...) basing on circuit's instructions
#simulator = Aer.get_backend("statevector_simulator") #simulator for returning the quantum state of output of circuit
#note: the statevector, density_matrix and unitary backends come also with a GPU option


# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:",counts)

# if information about particular consecutive results is needed
# important: moreover adding parameter memory=True in simulator.run(...) is needed
memory = result.get_memory(compiled_circuit)
print(memory)

# Draw the circuit
circuit.draw(output="mpl")  #or persistent file version => circuit.draw(output='mpl', filename='my_circuit.png')
plt.show()