from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import transpile
import numpy as np
import time
import random
from qiskit_aer.noise import NoiseModel
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
def phase_oracle(n):
    qc=QuantumCircuit(n)
    qc.h(n-1)
    qc.mcx(list(range(n-1)),n-1)
    qc.h(n-1)
    return qc

def diffuse(n):
    qc=QuantumCircuit(n)
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n-1)
    qc.mcx(list(range(n-1)),n-1)
    qc.h(n-1)
    qc.x(range(n))
    qc.h(range(n))
 return qc

def grover(n):
#apply diffusion operator
   qc=QuantumCircuit(n,n)
   qc.h(range(n))
   iterations=int(np.floor(np.pi/4*np.sqrt(2**n)))
   for _ in range(iterations):
     qc.compose(phase_oracle(n),inplace=True)
     qc.compose(diffuse(n),inplace=True) #combine phase oracle and diffusion circuits into one
     qc.measure(range(n),range(n))
   return qc


def classic_search(N):
   target=random.randint(0,N-1) #generate random int to search for
   start=time.time()
   for i in range(N):
       if i==target:
          break
   return time.time()-start


q=QuantumRegister(2,'q')
c=ClassicalRegister(2,'c')
qc=QuantumCircuit(2,2)
service=QiskitRuntimeService(channel="ibm_quantum_platform")
backend=service.least_busy(simulator=False)
noise_model=NoiseModel.from_backend(backend)
sim=AerSimulator(noise_model=noise_model)
for i in range(2,6):
    start=time.time()
    qc=grover(i)
    result=sim.run(qc,shots=1024).result() #run grover(1) 1024 times for first iteration of the for loop
    counts=result.get_counts()
    running_time=time.time()-start
    marked_state='1'*i
    success_ratio=counts.get(marked_state,0)/1024
    print(f"n={i}, success probability: {success_ratio}  running time:{running_time}")
for i in range(2,6):
    result=classic_search(i)
    print(f"total time for trial {i}: {running_time}")
