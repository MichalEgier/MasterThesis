
from qiskit import QuantumRegister, QuantumCircuit
import numpy as np
from qiskit.quantum_info import Kraus

def add_simple_error_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, index_of_error: int):
    circuit.x(logical[index_of_error])  # Bit flip error
    circuit.z(logical[index_of_error])  # Phase flip error

def add_identity_gates_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister):
    '''Noise is supposed to be assigned to identity gate through external NoiseModel'''
    circuit.id(logical)

def add_bit_phase_error_channel_subcircuit(circuit: QuantumCircuit, logical: QuantumRegister, p: float):
    '''Implementation with Kraus-operators representation'''

    #p = p/2 # due to fact that has been applied twice in this implementation

    # x channel
    K0 = np.array([[np.sqrt(p), 0], [0, np.sqrt(p)]])
    K1 = np.array([[0, np.sqrt(1-p)], [np.sqrt(1-p), 0]])

    x_channel = Kraus([K0,K1])

    # y channel
    K0 = np.array([[np.sqrt(p), 0], [0, np.sqrt(p)]])
    K1 = np.array([[np.sqrt(1-p), 0], [0, -1 * np.sqrt(1-p)]])

    y_channel = Kraus([K0,K1])

    #DODAC NAZWE DO TEGO !!! SPARAMETYZOWAC P !!!!
    total_channel = x_channel.compose(y_channel)

    for x in range(logical.size):
        circuit.append(total_channel.to_instruction(), [x])

    circuit.h(logical)
    for x in range(logical.size):
        circuit.append(total_channel.to_instruction(), [x])
    circuit.h(logical)
