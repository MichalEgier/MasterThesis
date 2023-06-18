
from qiskit import QuantumRegister, QuantumCircuit

def add_delay_to_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, delay_ns):
    circuit.delay(delay_ns, unit="ns")
    #circuit.h(logical)
    #circuit.delay(delay_ns, unit="ns")
    #circuit.h(logical)

