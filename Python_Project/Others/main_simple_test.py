
# Import Aer
from qiskit import *
from qiskit.extensions import Initialize
import numpy as np

# Run the quantum circuit on a statevector simulator backend
backend = Aer.get_backend('statevector_simulator')
#backend = Aer.get_backend("aer_simulator")

q = QuantumRegister(1)
c = ClassicalRegister(1)
circuit = QuantumCircuit(q, c)
circuit.initialize([1/np.sqrt(4), np.sqrt(3/4)], 0)

#circuit.x(0)
circuit.h(0)


job = execute(circuit, backend, shots=10000)
result = job.result()
outputstate = result.get_statevector(circuit, decimals=3)
print(outputstate)

#circuit.measure(q[0],c[0])
#job = backend.run(circuit)
#result = job.result().get_counts()
#print(result)