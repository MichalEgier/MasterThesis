
from qiskit import QuantumRegister, QuantumCircuit

def add_delay_to_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister):
    #circuit.delay(150000, unit="ns")
    circuit.h(logical)
    #circuit.delay(150000, unit="ns")
    circuit.h(logical)

