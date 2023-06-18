from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit, add_bit_phase_error_channel_subcircuit
from Common.utils import count_fidelity

def run_code(backend, delay_ns: int = 0, artifical_certain_error = False, shots = 100_000, artifical_probabilistic_error_rate = 0, initial_state = None, hadamard_basis = False, referential_0_state_measured_ratio=None):
    q = QuantumRegister(1, 'q')
    c = ClassicalRegister(1,'c')

    circuit = QuantumCircuit(q, c)

    if(initial_state):
        circuit.initialize(initial_state, 0)

    if(artifical_certain_error):
        add_simple_error_subcircuit(circuit, q, 0)
    if(delay_ns > 0):
        add_delay_to_subcircuit(circuit, q, delay_ns)
    if(artifical_probabilistic_error_rate > 0):
        add_bit_phase_error_channel_subcircuit(circuit, q, artifical_probabilistic_error_rate)


    circuit.barrier(q)

    if(hadamard_basis):
        circuit.h(0)
    circuit.measure(q[0], c[0])

    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()

    print("\n No code at all results:")
    print("--------------------------------------")
    print("Delay = ", delay_ns, "ns", "Artifical error rate = ", artifical_probabilistic_error_rate, "hadamard_basis", hadamard_basis, "initial_state=", initial_state)
    if(referential_0_state_measured_ratio):
        print("Fidelity = ", count_fidelity(counts, referential_0_state_measured_ratio))
    print(counts)

