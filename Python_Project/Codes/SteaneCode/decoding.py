from qiskit import QuantumCircuit, QuantumRegister

def add_decoding_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister):
    # firstly - simple decoding with reversal of encoding

    circuit.cx(logical[4], logical[3])
    circuit.cx(logical[4], logical[2])
    circuit.cx(logical[4], logical[1])

    circuit.cx(logical[5], logical[3])
    circuit.cx(logical[5], logical[2])
    circuit.cx(logical[5], logical[0])

    circuit.cx(logical[6], logical[3])
    circuit.cx(logical[6], logical[1])
    circuit.cx(logical[6], logical[0])

    circuit.cx(logical[0], logical[2])
    circuit.cx(logical[0], logical[1])

    circuit.h(logical[6])
    circuit.h(logical[5])
    circuit.h(logical[4])