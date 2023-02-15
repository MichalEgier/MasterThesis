from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def add_correction_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, x_syndrome: ClassicalRegister, z_syndrome: ClassicalRegister):
    for i in range(1, 8):
        circuit.x(logical[i - 1]).c_if(x_syndrome, i)

    # Apply the corrective Z gates
    for i in range(1, 8):
        circuit.z(logical[i - 1]).c_if(z_syndrome, i)
