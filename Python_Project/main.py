
from Common.utils import get_real_device_simulator_backend, get_perfect_gates_simulator_backend
from Codes import bit_flip_code_in_place, five_qubits_code, shorcode_in_place, sign_flip_code_in_place, steane_code_3_ancilla_reset, steane_code_6_ancilla
from Common import uncorrected_circuit

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


def run_real_device_simulator_experiments():
    backend = get_real_device_simulator_backend()
    shots = 100_000
    delay_times = [0, 1000, 5000, 10000, 15000]
    for t in delay_times:
        bit_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots)
        five_qubits_code.run_code(backend, delay_ns=t, shots=shots)
        shorcode_in_place.run_code(backend, delay_ns=t, shots=shots)
        sign_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots)
        steane_code_3_ancilla_reset.run_code(backend, delay_ns=t, shots=shots)
        steane_code_6_ancilla.run_code(backend, delay_ns=t, shots=shots)
        uncorrected_circuit.run_code(backend, delay_ns=t, shots=shots)

def run_perfect_gates_simulator_experiments():
    '''Although gates are simulated to be perfect, noise from environment is still present in these experiments.'''
    backend = get_perfect_gates_simulator_backend()
    shots = 100_000
    delay_times = [0, 1000, 5000, 10000, 15000]
    for t in delay_times:
        bit_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots)
        five_qubits_code.run_code(backend, delay_ns=t, shots=shots)
        shorcode_in_place.run_code(backend, delay_ns=t, shots=shots)
        sign_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots)
        steane_code_3_ancilla_reset.run_code(backend, delay_ns=t, shots=shots)
        steane_code_6_ancilla.run_code(backend, delay_ns=t, shots=shots)
        uncorrected_circuit.run_code(backend, delay_ns=t, shots=shots)


#run_real_device_simulator_experiments()
run_perfect_gates_simulator_experiments()

