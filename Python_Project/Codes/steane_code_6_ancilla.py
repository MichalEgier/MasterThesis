
print('\nSteane Code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import Aer

from Codes.SteaneCode.encoding import add_encoding_subcircuit
from Codes.SteaneCode.syndrome_measurement import add_syndrome_measurement_6_ancilla_subcircuit
from Codes.SteaneCode.correction import add_correction_subcircuit
from Codes.SteaneCode.decoding import add_decoding_subcircuit

import matplotlib.pyplot as plt

#IBMQ.enable_account(‘ENTER API KEY HERE')
#provider = IBMQ.get_provider(hub='ibm-q')

#backend = provider.get_backend('ibmq_qasm_simulator')

backend = Aer.get_backend("aer_simulator")




#####Steane code starts here ########
q_logical = QuantumRegister(7, 'logical')
ancilla = QuantumRegister(6, 'ancilla')
x_syndrome = ClassicalRegister(3, 'x_syndrome')
z_syndrome = ClassicalRegister(3, 'z_syndrome')
fin_m = ClassicalRegister(1,'final_measurement') #1 for final measurement after decoding, 6 ancilla for decoding (syndrome measurement)

circuit = QuantumCircuit(q_logical, ancilla, x_syndrome, z_syndrome, fin_m)

#q[0] is the state to encode

add_encoding_subcircuit(circuit, q_logical)
circuit.barrier()

####error here############
circuit.x(q_logical[6])#Bit flip error
circuit.z(q_logical[6])#Phase flip error
############################

circuit.barrier()
add_syndrome_measurement_6_ancilla_subcircuit(circuit, q_logical, ancilla)
circuit.barrier()
add_correction_subcircuit(circuit, q_logical, x_syndrome, z_syndrome)
circuit.barrier()
add_decoding_subcircuit(circuit, q_logical)

#here final measurement

circuit.barrier()
circuit.measure(q_logical[0], fin_m)

circuit.draw(output='mpl', filename='../Circuits/steane_code_6_ancilla.png') #Draws an image of the circuit

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\nSteane code with bit flip and phase error")
print("----------------------------------------")
print(counts)