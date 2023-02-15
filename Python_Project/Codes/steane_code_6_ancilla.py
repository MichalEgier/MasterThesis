print('\nSteane Code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer

import matplotlib.pyplot as plt

#IBMQ.enable_account(‘ENTER API KEY HERE')
#provider = IBMQ.get_provider(hub='ibm-q')

#backend = provider.get_backend('ibmq_qasm_simulator')

backend = Aer.get_backend("aer_simulator")

q = QuantumRegister(1,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.h(q[0])

####error here############
#circuit.x(q[0])#Bit flip error
#circuit.z(q[0])#Phase flip error
############################

circuit.h(q[0])

circuit.barrier(q)  #co to robi?

circuit.measure(q[0],c[0])

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\n Uncorrected bit flip and phase error")
print("--------------------------------------")
print(counts)

#####Steane code starts here ########
q = QuantumRegister(7+6,'q') #7 for encoding, 6 ancilla for decoding
#q = QuantumRegister(7,'q') #7 for encoding, 6 ancilla for decoding
#c = ClassicalRegister(1+6,'c') #1 for final measurement after decoding, 6 ancilla for decoding (syndrome measurement)
x_syndrome = ClassicalRegister(3, 'x_syndrome')
z_syndrome = ClassicalRegister(3, 'z_syndrome')
fin_m = ClassicalRegister(1,'final_measurement') #1 for final measurement after decoding, 6 ancilla for decoding (syndrome measurement)

circuit = QuantumCircuit(q, x_syndrome, z_syndrome, fin_m)

#q[0] is the state to encode

circuit.h(q[4])
circuit.h(q[5])
circuit.h(q[6])

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.cx(q[6],q[0])
circuit.cx(q[6],q[1])
circuit.cx(q[6],q[3])

circuit.cx(q[5],q[0])
circuit.cx(q[5],q[2])
circuit.cx(q[5],q[3])

circuit.cx(q[4],q[1])
circuit.cx(q[4],q[2])
circuit.cx(q[4],q[3])

circuit.barrier(q)

####error here############
circuit.x(q[6])#Bit flip error
circuit.z(q[6])#Phase flip error
############################

circuit.barrier(q)

# syndrome measurement here

circuit.cx(q[0],q[7])
circuit.cx(q[2],q[7])
circuit.cx(q[4],q[7])
circuit.cx(q[6],q[7])

circuit.cx(q[1],q[8])
circuit.cx(q[2],q[8])
circuit.cx(q[5],q[8])
circuit.cx(q[6],q[8])

circuit.cx(q[3],q[9])
circuit.cx(q[4],q[9])
circuit.cx(q[5],q[9])
circuit.cx(q[6],q[9])

circuit.h(q[10])
circuit.h(q[11])
circuit.h(q[12])

circuit.cx(q[10],q[0])
circuit.cx(q[10],q[2])
circuit.cx(q[10],q[4])
circuit.cx(q[10],q[6])

circuit.cx(q[11],q[1])
circuit.cx(q[11],q[2])
circuit.cx(q[11],q[5])
circuit.cx(q[11],q[6])

circuit.cx(q[12],q[3])
circuit.cx(q[12],q[4])
circuit.cx(q[12],q[5])
circuit.cx(q[12],q[6])

circuit.h(q[10])
circuit.h(q[11])
circuit.h(q[12])

circuit.measure(range(7,10), range(0,3)) #first 3 ancilla qubits (for bit-error measurement) to classical bits mapping (measurement)
circuit.measure(range(10,13), range(3,6)) #next 3 ancilla qubits (for phase-error measurement) to classical bits mapping (measurement)

circuit.barrier(q)

# correction here

for i in range(1, 8):
    circuit.x(q[i - 1]).c_if(x_syndrome, i)

# Apply the corrective Z gates
for i in range(1, 8):
    circuit.z(q[i - 1]).c_if(z_syndrome, i)

# decoding here

# firstly - simple decoding with reversal of encoding

circuit.cx(q[4],q[3])
circuit.cx(q[4],q[2])
circuit.cx(q[4],q[1])

circuit.cx(q[5],q[3])
circuit.cx(q[5],q[2])
circuit.cx(q[5],q[0])

circuit.cx(q[6],q[3])
circuit.cx(q[6],q[1])
circuit.cx(q[6],q[0])

circuit.cx(q[0],q[2])
circuit.cx(q[0],q[1])

circuit.h(q[6])
circuit.h(q[5])
circuit.h(q[4])

#here final measurement

circuit.barrier(q)

circuit.measure(q[0],fin_m)

circuit.draw(output='mpl', filename='../Circuits/steane_code_6_ancilla.png') #Draws an image of the circuit

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\nSteane code with bit flip and phase error")
print("----------------------------------------")
print(counts)
#input()

from qiskit.visualization import array_to_latex
from qiskit.quantum_info import Statevector

#state = Statevector.from_int(0, 2**7)
#state = state.evolve(circuit)
#print("",state.draw(output='text'))
#latex_str = state.draw(output='latex_source')
#print(latex_str)
#plt.plot()
#plt.text(0.5, 0.5, latex_str)
#plt.show()
#print(type(state.draw()))
#print("",state)
#array_to_latex(state)