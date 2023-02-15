from qiskit import QuantumCircuit, QuantumRegister

def add_decoding_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister):
    # firstly - simple decoding with reversal of encoding

    circuit.h(logical[1])
    circuit.h(logical[0])
    circuit.cnot(logical[2], logical[4])
    circuit.cnot(logical[1], logical[4])
    circuit.cnot(logical[0], logical[4])
    circuit.h(logical[3])
    circuit.h(logical[0])
    circuit.cnot(logical[2], logical[3])
    circuit.cnot(logical[0], logical[3])
    circuit.h(logical[2])
    circuit.cnot(logical[1], logical[2])
    circuit.cnot(logical[0], logical[2])
    circuit.h(logical[1])
    circuit.h(logical[0])
    circuit.cnot(logical[0], logical[1])
    circuit.z(logical[0])
    circuit.h(logical[0])
    circuit.z(logical[0])
