from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def add_syndrome_measurement_6_ancilla_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister, x_syndrome: ClassicalRegister, z_syndrome: ClassicalRegister) -> None:

    circuit.reset(ancilla[0:6])

    circuit.cx(logical[0], ancilla[0])
    circuit.cx(logical[2], ancilla[0])
    circuit.cx(logical[4], ancilla[0])
    circuit.cx(logical[6], ancilla[0])

    circuit.cx(logical[1], ancilla[1])
    circuit.cx(logical[2], ancilla[1])
    circuit.cx(logical[5], ancilla[1])
    circuit.cx(logical[6], ancilla[1])

    circuit.cx(logical[3], ancilla[2])
    circuit.cx(logical[4], ancilla[2])
    circuit.cx(logical[5], ancilla[2])
    circuit.cx(logical[6], ancilla[2])

    circuit.h(ancilla[3])
    circuit.h(ancilla[4])
    circuit.h(ancilla[5])

    circuit.cx(ancilla[3], logical[0])
    circuit.cx(ancilla[3], logical[2])
    circuit.cx(ancilla[3], logical[4])
    circuit.cx(ancilla[3], logical[6])

    circuit.cx(ancilla[4], logical[1])
    circuit.cx(ancilla[4], logical[2])
    circuit.cx(ancilla[4], logical[5])
    circuit.cx(ancilla[4], logical[6])

    circuit.cx(ancilla[5], logical[3])
    circuit.cx(ancilla[5], logical[4])
    circuit.cx(ancilla[5], logical[5])
    circuit.cx(ancilla[5], logical[6])

    circuit.h(ancilla[3])
    circuit.h(ancilla[4])
    circuit.h(ancilla[5])

    circuit.measure(ancilla[0:3], x_syndrome)
    circuit.measure(ancilla[3:6], z_syndrome)


def add_syndrome_measurement_3_ancilla_reset_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister, x_syndrome: ClassicalRegister, z_syndrome: ClassicalRegister) -> None:

    circuit.reset(ancilla[0:3])

    circuit.cx(logical[0], ancilla[0])
    circuit.cx(logical[2], ancilla[0])
    circuit.cx(logical[4], ancilla[0])
    circuit.cx(logical[6], ancilla[0])

    circuit.cx(logical[1], ancilla[1])
    circuit.cx(logical[2], ancilla[1])
    circuit.cx(logical[5], ancilla[1])
    circuit.cx(logical[6], ancilla[1])

    circuit.cx(logical[3], ancilla[2])
    circuit.cx(logical[4], ancilla[2])
    circuit.cx(logical[5], ancilla[2])
    circuit.cx(logical[6], ancilla[2])

    circuit.measure(ancilla[0:3], x_syndrome)

    circuit.reset(ancilla[0:3])

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])

    circuit.cx(ancilla[0], logical[0])
    circuit.cx(ancilla[0], logical[2])
    circuit.cx(ancilla[0], logical[4])
    circuit.cx(ancilla[0], logical[6])

    circuit.cx(ancilla[1], logical[1])
    circuit.cx(ancilla[1], logical[2])
    circuit.cx(ancilla[1], logical[5])
    circuit.cx(ancilla[1], logical[6])

    circuit.cx(ancilla[2], logical[3])
    circuit.cx(ancilla[2], logical[4])
    circuit.cx(ancilla[2], logical[5])
    circuit.cx(ancilla[2], logical[6])

    circuit.h(ancilla[0])
    circuit.h(ancilla[1])
    circuit.h(ancilla[2])

    circuit.measure(ancilla[0:3], z_syndrome)
