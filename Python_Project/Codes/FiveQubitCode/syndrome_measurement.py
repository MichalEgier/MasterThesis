from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def add_syndrome_measurement_4_ancilla_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister, syndrome: ClassicalRegister) -> None:

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])
    circuit.h(ancilla[3])

    circuit.cz(ancilla[0], [logical[index] for index in [1,4]])
    circuit.cx(ancilla[0], [logical[index] for index in [2,3]])

    circuit.cz(ancilla[1], [logical[index] for index in [0,2]])
    circuit.cx(ancilla[1], [logical[index] for index in [3,4]])

    circuit.cz(ancilla[2], [logical[index] for index in [1,3]])
    circuit.cx(ancilla[2], [logical[index] for index in [0,4]])

    circuit.cz(ancilla[3], [logical[index] for index in [2,4]])
    circuit.cx(ancilla[3], [logical[index] for index in [0,1]])

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])
    circuit.h(ancilla[3])

    circuit.measure(ancilla, syndrome)

'''
# v2 (wiki)
def add_syndrome_measurement_4_ancilla_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister, syndrome: ClassicalRegister) -> None:

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])
    circuit.h(ancilla[3])

    circuit.cz(ancilla[0], [logical[index] for index in [1,2]])
    circuit.cx(ancilla[0], [logical[index] for index in [0,3]])

    circuit.cz(ancilla[1], [logical[index] for index in [2,3]])
    circuit.cx(ancilla[1], [logical[index] for index in [1,4]])

    circuit.cz(ancilla[2], [logical[index] for index in [3,4]])
    circuit.cx(ancilla[2], [logical[index] for index in [0,2]])

    circuit.cz(ancilla[3], [logical[index] for index in [0,4]])
    circuit.cx(ancilla[3], [logical[index] for index in [1,3]])

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])
    circuit.h(ancilla[3])

    circuit.measure(ancilla, syndrome)
    '''