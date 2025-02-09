import matplotlib.pyplot as plt

input_sizes = [1000, 5000, 10000, 50000, 100000]
python_times = [0.00399, 0.02265, 0.05345, 0.31810, 0.68381]
c_times = [0.0001, 0.0006, 0.0013, 0.0072, 0.0150]

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, python_times, label="Python", marker='o')
plt.plot(input_sizes, c_times, label="C", marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Execution Time Comparison: Python vs C")
plt.legend()
plt.grid(True)
plt.show()