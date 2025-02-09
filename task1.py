import random
import matplotlib.pyplot as plt
import math

# Insertion Sort
def insertion_sort(arr):
    steps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            steps += 1
        arr[j + 1] = key
        steps += 1
    return steps

# Merge Sort
def merge_sort(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        steps = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            steps += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, steps

    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_steps = merge_sort(arr[:mid])
    right, right_steps = merge_sort(arr[mid:])
    merged, merge_steps = merge(left, right)
    total_steps = left_steps + right_steps + merge_steps
    return merged, total_steps

# Heap Sort
def heap_sort(arr):
    def heapify(arr, n, i):
        steps = 0
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps += 1
            steps += heapify(arr, n, largest)
        return steps

    n = len(arr)
    steps = 0
    for i in range(n // 2 - 1, -1, -1):
        steps += heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps += 1
        steps += heapify(arr, i, 0)
    return steps

# Quick Sort
def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        steps = 0
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps += 1
        return i + 1, steps

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi, steps = partition(arr, low, high)
            left_steps = quick_sort_helper(arr, low, pi - 1)
            right_steps = quick_sort_helper(arr, pi + 1, high)
            return steps + left_steps + right_steps
        return 0

    return quick_sort_helper(arr, 0, len(arr) - 1)


# Generate random input arrays of varying sizes
input_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
insertion_steps = []
merge_steps = []
heap_steps = []
quick_steps = []

for n in input_sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]
    
    # Insertion Sort
    steps = insertion_sort(arr.copy())
    insertion_steps.append(steps)
    
    # Merge Sort
    _, steps = merge_sort(arr.copy())
    merge_steps.append(steps)
    
    # Heap Sort
    steps = heap_sort(arr.copy())
    heap_steps.append(steps)
    
    # Quick Sort
    steps = quick_sort(arr.copy())
    quick_steps.append(steps)


# Plotting the results
plt.figure(figsize=(12, 8))

plt.plot(input_sizes, insertion_steps, label="Insertion Sort (Θ(n²))", marker='o')
plt.plot(input_sizes, merge_steps, label="Merge Sort (Θ(n log n))", marker='o')
plt.plot(input_sizes, heap_steps, label="Heap Sort (O(n log n))", marker='o')
plt.plot(input_sizes, quick_steps, label="Quick Sort (Θ(n²))", marker='o')

plt.xlabel("Input Size (n)")
plt.ylabel("Number of Steps")
plt.title("Number of Steps vs Input Size for Sorting Algorithms")
plt.legend()
plt.grid(True)
plt.show()