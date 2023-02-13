from qiskit import Aer
import numpy as np

# Import Qiskit
from qiskit import QuantumCircuit
from qiskit import Aer, transpile
from qiskit.tools.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi

# Generate a random Clifford C
num_qubits = 2
stab = qi.random_clifford(num_qubits, seed=100)

simulator = Aer.get_backend("aer_simulator")

# Set initial state to stabilizer state C|0>
circ = QuantumCircuit(num_qubits)
circ.set_stabilizer(stab)
circ.save_state()

# Transpile for simulator
circ = transpile(circ, simulator)

# Run and get saved data
result = simulator.run(circ).result()
print("result = ", result.data(0))

circ.draw(output='mpl',filename='stabilizer.png')