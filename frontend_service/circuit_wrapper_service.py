from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from circuit.circuit_wrapper import CircuitWrapper
import json
import sys

app = Flask(__name__)
cors = CORS(app)

@app.route('/circuit_to_internal', methods=['Post'])
def circuit_to_internal():
    data = request.json
    option = data["option"]
    circuit = data["circuit"]
    try:
        if option == "Quil":
            wrapper = CircuitWrapper(quil_str=circuit)
        elif option == "Pyquil":
            wrapper = CircuitWrapper(pyquil_instructions=circuit)
        elif option == "OpenQASM":
            wrapper = CircuitWrapper(qasm=circuit)
        elif option == "Qiskit":
            wrapper = CircuitWrapper(qiskit_instructions=circuit)
        else:
            return "Bad Request!", 400
        output = wrapper.export_qiskit_commands()    
    except Exception as e:
        print(str(e))
        return str(e), 500    
    return output

@app.route('/export_circuit', methods=['Post'])
def export_circuit():
    data = request.json
    option = data["option"]
    circuit = data["circuit"]
    try:
        wrapper = CircuitWrapper(qiskit_instructions=circuit) 
        if option == "Quil":
            output = wrapper.export_quil()
        elif option == "Pyquil":
            output = wrapper.export_pyquil()
        elif option == "OpenQASM":
            output = wrapper.export_qasm()
        elif option == "Qiskit":
            output = wrapper.export_qiskit_commands()
        else:
            return "Bad Request!", 400
    except Exception as e:
        print(str(e))
        return str(e), 500
    return output

@app.route('/convert', methods=['Post'])
def convert():
    data = request.json
    option = data["option"]
    option_output = data["optionOutput"]
    circuit = data["circuit"]
    try:
        if option == "Quil":
            wrapper = CircuitWrapper(quil_str=circuit)
        elif option == "Pyquil":
            wrapper = CircuitWrapper(pyquil_instructions=circuit)
        elif option == "OpenQASM":
            wrapper = CircuitWrapper(qasm=circuit)
        elif option == "Qiskit":
            wrapper = CircuitWrapper(qiskit_instructions=circuit)
        else:
            return "Bad Request!", 400

        if option_output == "Quil":
            output = wrapper.export_quil()
        elif option_output == "Pyquil":
            output = wrapper.export_pyquil()
        elif option_output == "OpenQASM":
            output = wrapper.export_qasm()
        elif option_output == "Qiskit":
            output = wrapper.export_qiskit_commands()
        else:
            return "Bad Request!", 400
    except Exception as e:
        print(str(e))
        return str(e), 500

    return output

@app.route('/unroll', methods=['Post'])
def unroll():
    data = request.json
    option = data["option"]
    nativeGates = data["nativeGates"]
    circuit = data["circuit"]
    try:
        wrapper = CircuitWrapper(qiskit_instructions=circuit)
        if option == "Rigetti":
            wrapper.unroll_rigetti()
        elif option == "IBMQ":
            wrapper.unroll_ibm()
        elif option == "Custom":
            wrapper.unroll(nativeGates)    
        else:
            return "Bad Request!", 400
        output = wrapper.export_qiskit_commands()

    except Exception as e:
        print(str(e))
        return str(e), 500
    
    return output

@app.route('/simulate', methods=['Post'])
def simulate():
    data = request.json
    circuit = data["circuit"]
    try:
        wrapper = CircuitWrapper(qiskit_instructions=circuit)
        output = wrapper.simulate()
    except Exception as e:
        print(str(e))
        return str(e), 500
    return output

@app.route('/depth', methods=['Post'])
def depth():
    data = request.json
    circuit = data["circuit"]
    try:
        depth = {}
        wrapper = CircuitWrapper(qiskit_instructions=circuit)
        wrapper.unroll_ibm()
        depth["q_depth"] = wrapper.depth()
        depth["q_two_qubit"] = wrapper.depth_two_qubit_gates()
        depth["q_gate_times"] = wrapper.depth_gate_times()

        wrapper = CircuitWrapper(qiskit_instructions=circuit)
        wrapper.unroll_rigetti()
        depth["r_depth"] = wrapper.depth()
        depth["r_two_qubit"] = wrapper.depth_two_qubit_gates()
        depth["r_gate_times"] = wrapper.depth_gate_times()
        output = depth
    except Exception as e:
        print(str(e))
        return str(e), 500
    return output



if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
