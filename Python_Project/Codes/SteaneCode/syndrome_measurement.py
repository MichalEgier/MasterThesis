from qiskit import QuantumCircuit, QuantumRegister

def add_syndrome_measurement_6_ancilla_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister) -> None:
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

    circuit.measure(range(7, 10), range(0,
                                        3))  # first 3 ancilla qubits (for bit-error measurement) to classical bits mapping (measurement)
    circuit.measure(range(10, 13), range(3,
                                         6))  # next 3 ancilla qubits (for phase-error measurement) to classical bits mapping (measurement)

def add_syndrome_measurement_3_ancilla_reset_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, ancilla: QuantumRegister) -> None:
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

    circuit.measure(range(7, 10), range(0,
                                        3))  # first 3 ancilla qubits (for bit-error measurement) to classical bits mapping (measurement)

    circuit.reset(range(7, 10))

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

    circuit.measure(range(7, 10), range(3,
                                         6))  # next 3 ancilla qubits (for phase-error measurement) to classical bits mapping (measurement)
