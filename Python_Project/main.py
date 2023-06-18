
from Common.utils import get_real_device_simulator_backend, get_perfect_gates_simulator_backend, get_identity_noise_model
from Codes import bit_flip_code_in_place, five_qubits_code, shorcode_in_place, sign_flip_code_in_place, steane_code_3_ancilla_reset, steane_code_6_ancilla
from Common import uncorrected_circuit
import numpy as np

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
    initial_state = [1 / np.sqrt(4), np.sqrt(3 / 4)]
    shots = 100_000
    delay_times = [0, 1000, 5000, 10000, 15000]
    for hadamard_basis_measurement in [True, False]:
        referential_0_state_measured_ratio = 0.966 * 0.966 if hadamard_basis_measurement else 0.25
        for t in delay_times:
            bit_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            five_qubits_code.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            shorcode_in_place.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            sign_flip_code_in_place.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            steane_code_3_ancilla_reset.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            steane_code_6_ancilla.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            uncorrected_circuit.run_code(backend, delay_ns=t, shots=shots, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)

def run_perfect_gates_simulator_experiments():
    '''Although gates are simulated to be perfect, noise from environment is still present in these experiments.'''
    backend = get_perfect_gates_simulator_backend()
    initial_state = [1 / np.sqrt(4), np.sqrt(3 / 4)]
    shots = 100_000
    error_rates = [0.001, 0.005, 0.01, 0.015, 0.05, 0.1]
    for hadamard_basis_measurement in [True, False]:
        referential_0_state_measured_ratio = 0.966 * 0.966 if hadamard_basis_measurement else 0.25
        for rate in error_rates:
            bit_flip_code_in_place.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)
            five_qubits_code.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio )
            shorcode_in_place.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio )
            sign_flip_code_in_place.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio )
            steane_code_3_ancilla_reset.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio )
            steane_code_6_ancilla.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio )
            uncorrected_circuit.run_code(backend, shots=shots, artifical_probabilistic_error_rate=rate, initial_state=initial_state, hadamard_basis=hadamard_basis_measurement, referential_0_state_measured_ratio=referential_0_state_measured_ratio)


#run_real_device_simulator_experiments()
run_perfect_gates_simulator_experiments()

