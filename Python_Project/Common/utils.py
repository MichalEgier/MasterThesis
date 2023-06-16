
from qiskit import QuantumCircuit

def construct_circuit(circuit: QuantumCircuit, subcircuits_appending_functions: list) -> None:
    subcircuits_appending_functions[0]()
    for f in subcircuits_appending_functions[1:]:
        circuit.barrier()
        f()

