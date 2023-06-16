from Codes.FiveQubitCode.correction import add_correction_subcircuit
from Codes.FiveQubitCode.decoding import add_decoding_subcircuit
from Codes.FiveQubitCode.encoding import add_encoding_subcircuit
from Codes.FiveQubitCode.syndrome_measurement import add_syndrome_measurement_4_ancilla_subcircuit
from Common.error_subcircuits import add_simple_error_subcircuit
from Common.delay_subcircuits import add_delay_to_subcircuit
from Common.utils import construct_circuit

print('\n5 Qubits code')
print('--------------')

from qiskit import QuantumRegister
from qiskit import ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import transpile
from Common.utils import get_simulator_backend, get_counts_without_syndrome


import matplotlib.pyplot as plt

# ================== General info ========================
#
#   In Place                            No
#   Mid-circuit measurement             Yes
#   Ancilla                             4
# ========================================================


#IBMQ.enable_account(‘ENTER API KEY HERE')
#provider = IBMQ.get_provider(hub='ibm-q')

#backend = provider.get_backend('ibmq_qasm_simulator')

#backend = Aer.get_backend("aer_simulator")
backend = get_simulator_backend()

#####Steane code starts here ########

#q_logical[0] is the state to encode

q_logical = QuantumRegister(5, '|0>')
ancilla = QuantumRegister(4, '|0> = ancilla')
syndrome = ClassicalRegister(4, 'syndrome')
fin_m = ClassicalRegister(1,'final_measurement')

circuit = QuantumCircuit(q_logical, ancilla, syndrome, fin_m)

construct_circuit(circuit, [
    lambda: add_encoding_subcircuit(circuit, q_logical),
    #lambda: add_simple_error_subcircuit(circuit, q_logical, 4),
    lambda: add_delay_to_subcircuit(circuit, q_logical),
    lambda: add_syndrome_measurement_4_ancilla_subcircuit(circuit, q_logical, ancilla, syndrome),
    lambda: add_correction_subcircuit(circuit, q_logical, syndrome),
    lambda: add_decoding_subcircuit(circuit, q_logical)
    ])

#here final measurement

circuit.barrier()
circuit.measure(q_logical[0], fin_m)

circuit.draw(output='mpl', filename='../Circuits/5_qubits_code.png') #Draws an image of the circuit

print(dict(circuit.count_ops()))

circuit = transpile(circuit, backend, optimization_level=3)
job = execute(circuit, backend, shots=100000)

job_monitor(job)

counts = job.result().get_counts()
counts_without_syndrome = get_counts_without_syndrome(counts)


print("\nSteane code with bit flip and phase error")
print("----------------------------------------")
print(counts)
print(counts_without_syndrome)