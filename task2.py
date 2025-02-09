import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Test execution time in Python
input_sizes = [1000, 5000, 10000, 50000, 100000]
python_times = []

for n in input_sizes:
    arr = [random.randint(0, 100000) for _ in range(n)]
    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    python_times.append(end_time - start_time)

print("Python Execution Times:", python_times)