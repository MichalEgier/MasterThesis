
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import transpile
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit



def run_code(backend, delay_ns: int = 0, artifical_error=False, shots=100_000):
    q = QuantumRegister(3,'q')
    c = ClassicalRegister(1,'c')

    circuit = QuantumCircuit(q,c)

    circuit.cx(q[0],q[1])
    circuit.cx(q[0],q[2])

    circuit.h(q[0])
    circuit.h(q[1])
    circuit.h(q[2])

    circuit.barrier()

    if(artifical_error):
        add_simple_error_subcircuit(circuit, q, 0)
    if(delay_ns > 0):
        add_delay_to_subcircuit(circuit, q, delay_ns)

    circuit.barrier()

    circuit.h(q[0])
    circuit.h(q[1])
    circuit.h(q[2])

    circuit.cx(q[0],q[1])
    circuit.cx(q[0],q[2])

    circuit.ccx(q[1],q[2],q[0])

    circuit.measure(q[0],c[0])

    circuit.draw(output='mpl',filename='Circuits/sign_flip_code_in_place.png') #Draws an image of the circuit

    print(dict(circuit.count_ops()))

    circuit = transpile(circuit, backend, optimization_level=3)
    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()

    print("\nSign flip code results:")
    print("----------------------------------------")
    print("Delay = ", delay_ns, "ns")
    print(counts)