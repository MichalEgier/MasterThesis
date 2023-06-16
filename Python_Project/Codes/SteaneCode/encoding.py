from qiskit import QuantumCircuit, QuantumRegister

def add_encoding_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister) -> None:
    circuit.h(logical[4])
    circuit.h(logical[5])
    circuit.h(logical[6])

    circuit.cx(logical[0],logical[1])
    circuit.cx(logical[0],logical[2])

    circuit.cx(logical[6],logical[0])
    circuit.cx(logical[6],logical[1])
    circuit.cx(logical[6],logical[3])

    circuit.cx(logical[5],logical[0])
    circuit.cx(logical[5],logical[2])
    circuit.cx(logical[5],logical[3])

    circuit.cx(logical[4],logical[1])
    circuit.cx(logical[4],logical[2])
    circuit.cx(logical[4],logical[3])



def add_encoding_fault_tolerant_with_flag_qubit_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister) -> None:
    '''Source: https://doi.org/10.3390/e24081107 '''
