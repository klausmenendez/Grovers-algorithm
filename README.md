# Grovers-algorithm
Grovers Algorithm: Classical vs Quantum Search Benchmark
This Project implements Grovers Search Algorithm and compares its performance to a classical  linear search algorithm. The goal is to experimentally demonstrate the Grover Search Algorithms O(n) query complexity relative to classical searches O(n) complexity. The experiment is performed with noise from ibm’s noise model


Motivations:
Grover’s algorithm provides a quadratic speedup for unstructured search problems. While the theoretical improvement for time complexity under Grover’s search algorithm is well known, this project investigates:
How query complexity scales with the size of the dataset provided
How execution time behaves in simulation
How noise impacts success ratio
This helps compare realistic performance on NISQ devices to theoretical quantum advantages

                                                                   
                                                                Methodology:
Classical Baseline:
Implemented a classical linear search algorithm with a size N data set
Measured:
    -Simulated execution time
     -number of oracle checks 
         Quantum Implementation
Implemented Grovers algorithm using a phase oracle and a diffusion operator 
Optimized the number of iterations to 4N
Measured:
    -success ratio
    -execution time
          Noise Model implementation:
Implemented Backend Noise Model via Qiskit AER
simulated:
      -Gate Error
      -Decoherence
      Compared noisy simulator vs ideal simulator
     
                                                             Results:
Verified Grovers algorithm scales with query complexity O(n^(1/2))
Verified classical linear search scales with query complexity O(n)
Observed severe degradation in success probability under realistic noise that gets worse with circuit depth
                                                Key findings:
Quantum speedup is visible in query complexity scaling 
Success rate decreases significantly with circuit depth under noise, making Grover's algorithm less reliable for larger circuits despite being faster

                                                      Technologies used:
Python 
Qiskit
Qiskit Aer
IBM backend noise models
Numpy

