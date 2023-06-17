
from qiskit import QuantumCircuit

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

def get_counts_without_syndrome(counts):
    counts_without_syndrome = {}
    from itertools import groupby
    for k, v in groupby(sorted(counts.items()), key=lambda i: 1 if i[0][0] == "1" else 0):
        counts_without_syndrome[k] = sum(item[1] for item in list(v))
    return counts_without_syndrome
