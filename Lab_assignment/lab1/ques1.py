import time
import matplotlib.pyplot as plt

def iterative_sum(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return sum

def recursive_sum(N):
    if N == 0:
        return 0
    return N + recursive_sum(N - 1)

# Measures time taken for both the algorithms
def measure_time(algorithm, N):
    start_time = time.time()
    algorithm(N)
    return time.time() - start_time

# Values of N to test
N_values = list(range(1, 1001, 50))

# Measure time for iterative and recursive algorithms
iterative_times = [measure_time(iterative_sum, N) for N in N_values]
recursive_times = [measure_time(recursive_sum, N) for N in N_values]

# Plotting
plt.plot(N_values, iterative_times, label='Iterative')
plt.plot(N_values, recursive_times, label='Recursive')
plt.xlabel('Value of N')
plt.ylabel('Time taken (seconds)')
plt.title('Time taken to calculate sum of first N natural numbers')
plt.legend()
plt.grid(True)
plt.show()
