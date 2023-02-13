from qutip.qip.circuit import QubitCircuit, Gate
from qutip import tensor, basis

'''
qc = QubitCircuit(N=2, num_cbits=1)
swap_gate = Gate(name="SWAP", targets=[0, 1])

qc.add_gate(swap_gate)
qc.add_measurement("M0", targets=[1], classical_store=0) # measurement gate
qc.add_gate("CNOT", controls=0, targets=1)
qc.add_gate("X", targets=0, classical_controls=[0]) # classically controlled gate
qc.add_gate(swap_gate)

print(qc.gates)
'''

qc = QubitCircuit(N=1, num_cbits=1)
print(qc.gates)
qc.add_gate(Gate("SNOT", targets=0))
qc.add_gate(Gate("SNOT", targets=0))
#qc.add_measurement("M0", targets=[0])
zero_state = basis(2,0)
result = qc.run(state=zero_state)
print(result)

#print(qc.gates)
#qc.png