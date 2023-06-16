print('\nBit flip code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import transpile
from Common.utils import get_simulator_backend
from Common.delay_subcircuits import add_delay_to_subcircuit

# local simulator
#backend = Aer.get_backend("aer_simulator")

# IBM's latest calibration snapshot of real device simulator
#from qiskit_aer import AerSimulator
#with open("apitoken.txt", "r") as f:
#    token = f.readline().strip()
#IBMQ.enable_account(token)
#provider = IBMQ.get_provider()
#device = provider.get_backend('ibmq_manila')
#backend = AerSimulator.from_backend(device)A

# IBM's old snapshots
backend = get_simulator_backend()

q = QuantumRegister(3,'|0>')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.barrier()

####error here############
#circuit.x(q[0])#Bit flip error
#circuit.z(q[0])#Phase flip error
############################

add_delay_to_subcircuit(circuit, q)

circuit.barrier()

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.ccx(q[1],q[2],q[0])

circuit.measure(q[0],c[0])

circuit.draw(output='mpl', filename='../Circuits/bit_flip_code_in_place.png') #Draws an image of the circuit

print(dict(circuit.count_ops()))

circuit = transpile(circuit, backend, optimization_level=3)
job = execute(circuit, backend, shots=100000)

job_monitor(job)

counts = job.result().get_counts()

print("\nBit flip code with bit flip and phase error")
print("----------------------------------------")
print(counts)
input("Press any key to continue ...")