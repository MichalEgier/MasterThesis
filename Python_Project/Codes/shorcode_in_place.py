print('\nShor Code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer
from qiskit import transpile
from Common.utils import get_simulator_backend
from Common.delay_subcircuits import add_delay_to_subcircuit

#IBMQ.enable_account(‘ENTER API KEY HERE')
#provider = IBMQ.get_provider(hub='ibm-q')

#backend = provider.get_backend('ibmq_qasm_simulator')

#backend = Aer.get_backend("aer_simulator")
backend = get_simulator_backend()

q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0])

####error here############
#circuit.x(q[0])#Bit flip error
#circuit.z(q[0])#Phase flip error
############################

add_delay_to_subcircuit(circuit, q)

circuit.h(q[0])

circuit.barrier(q)  #co to robi?

circuit.measure(q[0],c[0])

job = execute(circuit, backend, shots=10000)

job_monitor(job)

counts = job.result().get_counts()

print("\n Uncorrected bit flip and phase error")
print("--------------------------------------")
print(counts)

#####Shor code starts here ########
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

####error here############
#circuit.x(q[0])#Bit flip error
#circuit.z(q[0])#Phase flip error
############################

add_delay_to_subcircuit(circuit, q)

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

circuit.draw(output='mpl',filename='../Circuits/shorcode_in_place.png') #Draws an image of the circuit

print(dict(circuit.count_ops()))

circuit = transpile(circuit, backend, optimization_level=3)
job = execute(circuit, backend, shots=10000)

job_monitor(job)

counts = job.result().get_counts()

print("\nShor code with bit flip and phase error")
print("----------------------------------------")
print(counts)
input()