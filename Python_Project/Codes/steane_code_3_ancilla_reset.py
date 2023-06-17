
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer
from qiskit import transpile

from Codes.SteaneCode.encoding import add_encoding_subcircuit
from Codes.SteaneCode.syndrome_measurement import add_syndrome_measurement_3_ancilla_reset_subcircuit
from Codes.SteaneCode.correction import add_correction_subcircuit
from Codes.SteaneCode.decoding import add_decoding_subcircuit

from Common.utils import get_counts_without_syndrome
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit, add_bit_phase_error_channel_subcircuit
from Common.utils import construct_circuit

import matplotlib.pyplot as plt

# ================== General info ========================
#
#   In Place                            No
#   Mid-circuit measurement             Yes
#   Ancilla                             3
# ========================================================


def run_code(backend, delay_ns: int = 0, artifical_certain_error = False, shots = 100_000, artifical_probabilistic_error_rate = 0):

    q_logical = QuantumRegister(7, 'logical')
    ancilla = QuantumRegister(3, 'ancilla')
    x_syndrome = ClassicalRegister(3, 'x_syndrome')
    z_syndrome = ClassicalRegister(3, 'z_syndrome')
    fin_m = ClassicalRegister(1,'final_measurement') #1 for final measurement after decoding, 6 ancilla for decoding (syndrome measurement)

    circuit = QuantumCircuit(q_logical, ancilla, x_syndrome, z_syndrome, fin_m)

    construct_circuit(circuit, [
        lambda: add_encoding_subcircuit(circuit, q_logical),
        (lambda: add_simple_error_subcircuit(circuit, q_logical, 4)) if artifical_certain_error else None,
        (lambda: add_delay_to_subcircuit(circuit, q_logical, delay_ns)) if delay_ns > 0 else None,
        (lambda: add_bit_phase_error_channel_subcircuit(circuit, q_logical, artifical_probabilistic_error_rate) if artifical_probabilistic_error_rate > 0 else None),
        lambda: add_syndrome_measurement_3_ancilla_reset_subcircuit(circuit, q_logical, ancilla, x_syndrome, z_syndrome),
        lambda: add_correction_subcircuit(circuit, q_logical, x_syndrome, z_syndrome),
        lambda: add_decoding_subcircuit(circuit, q_logical)
        ])

    #here final measurement

    circuit.barrier()
    circuit.measure(q_logical[0], fin_m)

    circuit.draw(output='mpl', filename='Circuits/steane_code_3_ancilla_reset.png') #Draws an image of the circuit

    print(dict(circuit.count_ops()))

    circuit = transpile(circuit, backend, optimization_level=0 if artifical_probabilistic_error_rate > 0 else 3)
    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()
    counts_without_syndrome = get_counts_without_syndrome(counts)

    print("\nSteane code 3 ancilla results:")
    print("----------------------------------------")
    print("Delay = ", delay_ns, "ns", "Artifical error rate = ", artifical_probabilistic_error_rate)
    print(counts)
    print(counts_without_syndrome)