
from qiskit import QuantumCircuit
from qiskit_aer.noise import pauli_error, NoiseModel

def construct_circuit(circuit: QuantumCircuit, subcircuits_appending_functions: list) -> None:
    if(subcircuits_appending_functions[0]):
        subcircuits_appending_functions[0]()
    for f in subcircuits_appending_functions[1:]:
        if(f):
            circuit.barrier()
            f()

def get_real_device_simulator_backend():
    from qiskit.providers.fake_provider import FakeKolkataV2
    from qiskit_aer import AerSimulator
    fake_device = FakeKolkataV2()
    backend = AerSimulator.from_backend(fake_device)
    return backend

def get_perfect_gates_simulator_backend():
    from qiskit import Aer
    backend = Aer.get_backend("aer_simulator")
    return backend

def get_identity_noise_model(error_rate):
    bit_flip = pauli_error([('X', error_rate), ('I', 1 - error_rate)])
    phase_flip = pauli_error([('Z', error_rate), ('I', 1 - error_rate)])
    bit_phase_flip = bit_flip.compose(phase_flip)
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(bit_phase_flip, ['id'])
    #to delete
    print(noise_model)
    return noise_model

def get_counts_without_syndrome(counts):
    counts_without_syndrome = {}
    from itertools import groupby
    for k, v in groupby(sorted(counts.items()), key=lambda i: 1 if i[0][0] == "1" else 0):
        counts_without_syndrome[k] = sum(item[1] for item in list(v))
    return counts_without_syndrome
