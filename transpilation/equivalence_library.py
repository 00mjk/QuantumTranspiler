from qiskit.circuit.equivalence_library import EquivalenceLibrary
import qiskit.circuit.library.standard_gates as Gates
from qiskit import QuantumCircuit
import numpy as np
from qiskit.circuit import Parameter
from qiskit.circuit.equivalence_library import SessionEquivalenceLibrary

class EquivalenceLibraryBasis(EquivalenceLibrary):
    """
    define a equivalence library for several basis gates
    if all equivalence classes are written to the same library the unroller class has infinite loops and the language to solve it is semi-decidable
    """
    def __init__(self, gates):
        super().__init__()
        if "cz" in gates:
            self._cz()
        if "rx" and "rz" in gates:
            self._rx_rz()
    
    def _cz(self):
        # cx
        circuit = QuantumCircuit(2)
        circuit.h(1)
        circuit.cz(0, 1)
        circuit.h(1)
        self.add_equivalence(Gates.CXGate(), circuit)

    
    def _rx_rz(self):
        # u2
        # https://qiskit.org/documentation/stubs/qiskit.circuit.library.U2Gate.html#qiskit.circuit.library.U2Gate
        phi = Parameter("phi")
        lam = Parameter("lam")
        circuit = QuantumCircuit(1)
        circuit.rz(phi + np.pi/2, 0)
        circuit.rx(np.pi/2, 0)
        circuit.rz(lam - np.pi/2, 0)
        self.add_equivalence(Gates.U2Gate(phi, lam), circuit)

        # u3
        """implemented with two X90 pulse: https://arxiv.org/pdf/1707.03429.pdf"""        
        theta = Parameter("theta")
        phi = Parameter("phi")
        lam = Parameter("lambda")
        circuit = QuantumCircuit(1)
        circuit.rz(phi + 3*np.pi, 0)
        circuit.rx(np.pi/2, 0)
        circuit.rz(np.pi + theta, 0)
        circuit.rx(np.pi/2, 0)
        circuit.rz(lam, 0)
        # formula from https://qiskit.org/documentation/stubs/qiskit.circuit.library.U3Gate.html (13.07.2020) gives wrong results 
        # theta = Parameter("theta")
        # phi = Parameter("phi")
        # lam = Parameter("lambda")
        # circuit = QuantumCircuit(1)
        # circuit.rz(phi - np.pi/2, 0)
        # circuit.rx(np.pi/2, 0)
        # circuit.rz(np.pi - theta, 0)
        # circuit.rx(np.pi/2, 0)
        # circuit.rz(lam - np.pi/2, 0)        
        self.add_equivalence(Gates.U3Gate(theta, phi, lam), circuit)


    