from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer

backend = Aer.get_backend("aer_simulator")

q = QuantumRegister(1, 'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q, c)

circuit.h(q[0])

####error here############
#circuit.x(q[0])#Bit flip error
#circuit.z(q[0])#Phase flip error
############################

circuit.h(q[0])

circuit.barrier(q)  #co to robi?

circuit.measure(q[0], c[0])

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\n Uncorrected bit flip and phase error")
print("--------------------------------------")
print(counts)

