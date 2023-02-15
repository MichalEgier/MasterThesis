
from qiskit import QuantumRegister, QuantumCircuit

def add_simple_error_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, index_of_error: int):
    circuit.x(logical[index_of_error])  # Bit flip error
    circuit.z(logical[index_of_error])  # Phase flip error