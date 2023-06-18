from Codes.FiveQubitCode.correction import add_correction_subcircuit
from Codes.FiveQubitCode.decoding import add_decoding_subcircuit
from Codes.FiveQubitCode.encoding import add_encoding_subcircuit
from Codes.FiveQubitCode.syndrome_measurement import add_syndrome_measurement_4_ancilla_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit, add_bit_phase_error_channel_subcircuit
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.utils import construct_circuit

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import transpile
from Common.utils import get_counts_without_syndrome
from Common.utils import count_fidelity


import matplotlib.pyplot as plt

# ================== General info ========================
#
#   In Place                            No
#   Mid-circuit measurement             Yes
#   Ancilla                             4
# ========================================================


def run_code(backend, delay_ns: int = 0, artifical_certain_error = False, shots = 100_000, artifical_probabilistic_error_rate = 0, initial_state = None, hadamard_basis = False, referential_0_state_measured_ratio=None):

    q_logical = QuantumRegister(5, '|0>')
    ancilla = QuantumRegister(4, '|0> = ancilla')
    syndrome = ClassicalRegister(4, 'syndrome')
    fin_m = ClassicalRegister(1,'final_measurement')

    circuit = QuantumCircuit(q_logical, ancilla, syndrome, fin_m)

    if(initial_state):
        circuit.initialize(initial_state, 0)

    construct_circuit(circuit, [
        lambda: add_encoding_subcircuit(circuit, q_logical),
        (lambda: add_simple_error_subcircuit(circuit, q_logical, 4)) if artifical_certain_error else None,
        (lambda: add_delay_to_subcircuit(circuit, q_logical, delay_ns)) if delay_ns > 0 else None,
        (lambda: add_bit_phase_error_channel_subcircuit(circuit, q_logical, artifical_probabilistic_error_rate) if artifical_probabilistic_error_rate > 0 else None),
        lambda: add_syndrome_measurement_4_ancilla_subcircuit(circuit, q_logical, ancilla, syndrome),
        lambda: add_correction_subcircuit(circuit, q_logical, syndrome),
        lambda: add_decoding_subcircuit(circuit, q_logical)
        ])

    #here final measurement

    circuit.barrier()

    if(hadamard_basis):
        circuit.h(0)
    circuit.measure(q_logical[0], fin_m)

    circuit.draw(output='mpl', filename='Circuits/5_qubits_code.png') #Draws an image of the circuit

    print(dict(circuit.count_ops()))

    circuit = transpile(circuit, backend, optimization_level=0 if artifical_probabilistic_error_rate > 0 else 3)
    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()
    counts_without_syndrome = get_counts_without_syndrome(counts)


    print("\n5-qubit code results:")
    print("----------------------------------------")
    print("Delay = ", delay_ns, "ns", "Artifical error rate = ", artifical_probabilistic_error_rate, "hadamard_basis", hadamard_basis, "initial_state=", initial_state)
    if(referential_0_state_measured_ratio):
        print("Fidelity = ", count_fidelity(counts_without_syndrome, referential_0_state_measured_ratio))
    print(counts)
    print(counts_without_syndrome)