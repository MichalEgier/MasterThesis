from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit

def run_code(backend, delay_ns: int = 0, artifical_error = False, shots = 100_000):
    q = QuantumRegister(1, 'q')
    c = ClassicalRegister(1,'c')

    circuit = QuantumCircuit(q, c)

    circuit.h(q[0])

    if(artifical_error):
        add_simple_error_subcircuit(circuit, q, 0)
    if(delay_ns > 0):
        add_delay_to_subcircuit(circuit, q, delay_ns)

    circuit.h(q[0])

    circuit.barrier(q)

    circuit.measure(q[0], c[0])

    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()

    print("\n No code at all results:")
    print("--------------------------------------")
    print("Delay = ", delay_ns, "ns")
    print(counts)

