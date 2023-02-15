from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def add_correction_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, syndrome: ClassicalRegister):

    def _add_correction(logical_qubit_index, binary_syndrome: str, error_type: str):
        qubit = logical[logical_qubit_index]
        switcher = {
            'x': circuit.x(qubit),
            'z': circuit.z(qubit),
            'y': circuit.y(qubit)
        }
        switcher.get(error_type).c_if(syndrome, int(binary_syndrome, 2))

    x_pairs = [(0, '0010'), (1, '0101'), (2, '1010'), (3, '0100'), (4, '1001')]
    z_pairs = [(0, '1100'), (1, '1000'), (2, '0001'), (3, '0011'), (4, '0110')]
    y_pairs = [(0, '1110'), (1, '1101'), (2, '1011'), (3, '0111'), (4, '1111')]

    for e in x_pairs:
        _add_correction(e[0], e[1], 'x')

    for e in z_pairs:
        _add_correction(e[0], e[1], 'z')

    for e in y_pairs:
        _add_correction(e[0], e[1], 'y')

    '''
    left: index of X, right: binary represented number in syndrome
    X:
        0 -> 0010
        1 -> 0101
        2 -> 1010
        3 -> 0100
        4 -> 1001
    Z:
        0 -> 1100
        1 -> 1000
        2 -> 0001
        3 -> 0011
        4 -> 0110
    Y:
        0 -> 1110
        1 -> 1101
        2 -> 1011
        3 -> 0111
        4 -> 1111
    '''
