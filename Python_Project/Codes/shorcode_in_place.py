
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer
from qiskit import transpile
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit, add_bit_phase_error_channel_subcircuit

def run_code(backend, delay_ns: int = 0, artifical_certain_error = False, shots = 100_000, artifical_probabilistic_error_rate = 0):

    q = QuantumRegister(9,'q')
    c = ClassicalRegister(1,'c')

    circuit = QuantumCircuit(q,c)

    # encoding

    circuit.cx(q[0],q[3])
    circuit.cx(q[0],q[6])

    circuit.h(q[0])
    circuit.h(q[3])
    circuit.h(q[6])

    circuit.cx(q[0],q[1])
    circuit.cx(q[3],q[4])
    circuit.cx(q[6],q[7])

    circuit.cx(q[0],q[2])
    circuit.cx(q[3],q[5])
    circuit.cx(q[6],q[8])

    circuit.barrier(q)

    if(artifical_certain_error):
        add_simple_error_subcircuit(circuit, q, 0)
    if(delay_ns > 0):
        add_delay_to_subcircuit(circuit, q, delay_ns)
    if(artifical_probabilistic_error_rate > 0):
        add_bit_phase_error_channel_subcircuit(circuit, q, artifical_probabilistic_error_rate)

    circuit.barrier(q)

    # decoding

    circuit.cx(q[0],q[1])
    circuit.cx(q[3],q[4])
    circuit.cx(q[6],q[7])

    circuit.cx(q[0],q[2])
    circuit.cx(q[3],q[5])
    circuit.cx(q[6],q[8])

    circuit.ccx(q[1],q[2],q[0])
    circuit.ccx(q[4],q[5],q[3])
    circuit.ccx(q[8],q[7],q[6])

    circuit.h(q[0])
    circuit.h(q[3])
    circuit.h(q[6])

    circuit.cx(q[0],q[3])
    circuit.cx(q[0],q[6])
    circuit.ccx(q[6],q[3],q[0])

    circuit.barrier(q)

    circuit.measure(q[0],c[0])

    circuit.draw(output='mpl',filename='Circuits/shorcode_in_place.png') #Draws an image of the circuit

    print(dict(circuit.count_ops()))

    circuit = transpile(circuit, backend, optimization_level=0 if artifical_probabilistic_error_rate > 0 else 3)
    job = execute(circuit, backend, shots=shots)

    job_monitor(job)

    counts = job.result().get_counts()

    print("\nShor code results:")
    print("----------------------------------------")
    print("Delay = ", delay_ns, "ns", "Artifical error rate = ", artifical_probabilistic_error_rate)
    print(counts)