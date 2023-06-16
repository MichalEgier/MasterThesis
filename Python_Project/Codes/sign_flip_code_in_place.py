print('\nSign flip code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer

#IBMQ.enable_account(‘ENTER API KEY HERE')
#provider = IBMQ.get_provider(hub='ibm-q')

#backend = provider.get_backend('ibmq_qasm_simulator')

backend = Aer.get_backend("aer_simulator")

q = QuantumRegister(3,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])

circuit.barrier()

####error here############
#circuit.x(q[0])#Bit flip error
circuit.z(q[0])#Phase flip error
############################

circuit.barrier()

circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.ccx(q[1],q[2],q[0])

circuit.measure(q[0],c[0])

circuit.draw(output='mpl',filename='../Circuits/sign_flip_code_in_place.png') #Draws an image of the circuit

print(dict(circuit.count_ops()))

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\nSign flip code with bit flip and phase error")
print("----------------------------------------")
print(counts)
input()