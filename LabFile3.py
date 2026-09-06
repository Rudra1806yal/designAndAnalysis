
# Graphs and Visualizations Comparing Execution Time
# and Memory Consumption of Sorting and Fibonacci Algorithms

import time
import tracemalloc
import random
import matplotlib.pyplot as plt


# ============================================================
# SORTING ALGORITHMS
# ============================================================

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# ============================================================
# FIBONACCI ALGORITHMS
# ============================================================

def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


def fibonacci_dynamic(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ============================================================
# PERFORMANCE MEASUREMENT FUNCTION
# ============================================================

def measure_performance(function, *args):
    """
    Measures:
    1. Execution time in milliseconds
    2. Peak memory consumption in KB
    """

    tracemalloc.start()

    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    execution_time = (end_time - start_time) * 1000
    memory_usage = peak / 1024

    return execution_time, memory_usage, result


# ============================================================
# SORTING PERFORMANCE TEST
# ============================================================

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

sorting_sizes = [100, 500, 1000, 2000, 5000]

sorting_time = {name: [] for name in sorting_algorithms}
sorting_memory = {name: [] for name in sorting_algorithms}

print("=" * 70)
print("SORTING ALGORITHMS PERFORMANCE")
print("=" * 70)

for size in sorting_sizes:

    # Same input data for fair comparison
    data = [random.randint(1, 100000) for _ in range(size)]

    print(f"\nInput Size: {size}")

    for name, algorithm in sorting_algorithms.items():

        # Avoid very large input for slow O(n²) algorithms
        if name in ["Bubble Sort", "Insertion Sort"] and size > 2000:
            sorting_time[name].append(None)
            sorting_memory[name].append(None)
            print(f"{name:<20}: Skipped for large input")
            continue

        execution_time, memory_usage, result = measure_performance(
            algorithm, data
        )

        sorting_time[name].append(execution_time)
        sorting_memory[name].append(memory_usage)

        print(
            f"{name:<20}: "
            f"Time = {execution_time:.4f} ms, "
            f"Memory = {memory_usage:.2f} KB"
        )


# ============================================================
# FIBONACCI PERFORMANCE TEST
# ============================================================

fibonacci_algorithms = {
    "Recursive Fibonacci": fibonacci_recursive,
    "Iterative Fibonacci": fibonacci_iterative,
    "Dynamic Fibonacci": fibonacci_dynamic
}

# Recursive Fibonacci becomes extremely slow for large n
fib_sizes = [5, 10, 15, 20, 25, 30, 35]

fib_time = {name: [] for name in fibonacci_algorithms}
fib_memory = {name: [] for name in fibonacci_algorithms}

print("\n")
print("=" * 70)
print("FIBONACCI ALGORITHMS PERFORMANCE")
print("=" * 70)

for n in fib_sizes:

    print(f"\nFibonacci n = {n}")

    for name, algorithm in fibonacci_algorithms.items():

        execution_time, memory_usage, result = measure_performance(
            algorithm, n
        )

        fib_time[name].append(execution_time)
        fib_memory[name].append(memory_usage)

        print(
            f"{name:<25}: "
            f"Time = {execution_time:.4f} ms, "
            f"Memory = {memory_usage:.2f} KB"
        )


# ============================================================
# GRAPH 1: SORTING EXECUTION TIME
# ============================================================

plt.figure(figsize=(10, 6))

for name in sorting_algorithms:

    plt.plot(
        sorting_sizes,
        sorting_time[name],
        marker="o",
        linewidth=2,
        label=name
    )

plt.title("Sorting Algorithms - Execution Time")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (ms)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("sorting_execution_time.png", dpi=300)
plt.show()


# ============================================================
# GRAPH 2: SORTING MEMORY CONSUMPTION
# ============================================================

plt.figure(figsize=(10, 6))

for name in sorting_algorithms:

    plt.plot(
        sorting_sizes,
        sorting_memory[name],
        marker="o",
        linewidth=2,
        label=name
    )

plt.title("Sorting Algorithms - Memory Consumption")
plt.xlabel("Input Size")
plt.ylabel("Peak Memory (KB)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("sorting_memory_consumption.png", dpi=300)
plt.show()


# ============================================================
# GRAPH 3: FIBONACCI EXECUTION TIME
# ============================================================

plt.figure(figsize=(10, 6))

for name in fibonacci_algorithms:

    plt.plot(
        fib_sizes,
        fib_time[name],
        marker="o",
        linewidth=2,
        label=name
    )

plt.title("Fibonacci Algorithms - Execution Time")
plt.xlabel("Fibonacci Input (n)")
plt.ylabel("Execution Time (ms)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("fibonacci_execution_time.png", dpi=300)
plt.show()


# ============================================================
# GRAPH 4: FIBONACCI MEMORY CONSUMPTION
# ============================================================

plt.figure(figsize=(10, 6))

for name in fibonacci_algorithms:

    plt.plot(
        fib_sizes,
        fib_memory[name],
        marker="o",
        linewidth=2,
        label=name
    )

plt.title("Fibonacci Algorithms - Memory Consumption")
plt.xlabel("Fibonacci Input (n)")
plt.ylabel("Peak Memory (KB)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig("fibonacci_memory_consumption.png", dpi=300)
plt.show()

# ============================================================
# FINAL SUMMARY TABLE
# ============================================================

print("\n")
print("=" * 70)
print("ALGORITHM COMPLEXITY SUMMARY")
print("=" * 70)

print("""
+----------------------+--------------+---------------+
| Algorithm            | Time         | Extra Space   |
+----------------------+--------------+---------------+
| Bubble Sort          | O(n²)        | O(1)          |
| Insertion Sort       | O(n²)        | O(1)          |
| Merge Sort           | O(n log n)   | O(n)          |
| Quick Sort           | O(n log n)*  | O(n)*         |
| Recursive Fibonacci  | O(2^n)       | O(n)          |
| Iterative Fibonacci  | O(n)         | O(1)          |
| Dynamic Fibonacci    | O(n)        | O(n)          |
+----------------------+--------------+---------------+

* Average-case complexity for Quick Sort.
""")
