pip install matplotlib pandas

import time
import tracemalloc
import heapq
import matplotlib.pyplot as plt
import pandas as pd

#function of selection activity
def activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    selected = []
    last_finish = -1

    for name, start, finish in activities:
        if start >= last_finish:
            selected.append((name, start, finish))
            last_finish = finish

    return selected

#function of fractional knapsack
def fractional_knapsack(items, capacity):
    # Item format: (name, weight, value)
    items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)

    allocation = []
    total_value = 0

    for name, weight, value in items:
        if capacity <= 0:
            break

        taken = min(weight, capacity)
        total_value += value * (taken / weight)
        allocation.append((name, taken, weight))
        capacity -= taken

    return allocation, total_value

#function for huffman tree
def build_huffman_tree(frequencies):
    heap = []
    counter = 0

    for char, freq in frequencies.items():
        heapq.heappush(heap, (freq, counter, char))
        counter += 1

    tree = {}

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        node = f"Node{counter}"
        tree[node] = (left, right)

        heapq.heappush(heap, (f1 + f2, counter, node))
        counter += 1

    return heap[0][2], tree

#function for huffman graph tree
def draw_huffman_tree(root, tree, frequencies):
    positions = {}
    labels = {}
    edges = []

    def layout(node, depth, x_counter):
        if node not in tree:
            positions[node] = (x_counter[0], -depth)
            labels[node] = f"{node}\n({frequencies[node]})"
            x_counter[0] += 1
            return positions[node][0]

        left, right = tree[node]
        lx = layout(left, depth + 1, x_counter)
        rx = layout(right, depth + 1, x_counter)

        positions[node] = ((lx + rx) / 2, -depth)
        labels[node] = node
        edges.append((node, left, "0"))
        edges.append((node, right, "1"))
        return positions[node][0]

    layout(root, 0, [0])

    plt.figure(figsize=(12, 6))

    for parent, child, bit in edges:
        x1, y1 = positions[parent]
        x2, y2 = positions[child]

        plt.plot([x1, x2], [y1, y2], marker="o")
        plt.text((x1 + x2) / 2, (y1 + y2) / 2, bit)

    for node, (x, y) in positions.items():
        plt.text(
            x, y, labels[node],
            ha="center", va="center",
            bbox=dict(boxstyle="round", facecolor="white")
        )

    plt.title("Huffman Coding Tree")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

#function for measure performance
def measure_performance(algorithm, *args):
    tracemalloc.start()
    start = time.perf_counter()

    result = algorithm(*args)

    elapsed = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, elapsed, peak / 1024

    #main program
items = [
    ("A", 10, 60),
    ("B", 20, 100),
    ("C", 30, 120)
]

capacity = 50

allocation, total_value = fractional_knapsack(items, capacity)

print("Allocation:", allocation)
print("Total Value:", total_value)

frequencies = {
    "A": 5,
    "B": 9,
    "C": 12,
    "D": 13,
    "E": 16,
    "F": 45
}

root, huffman_tree = build_huffman_tree(frequencies)
draw_huffman_tree(root, huffman_tree, frequencies)

sizes = [100, 500, 1000, 2000, 5000]

execution_times = []
memory_usages = []

for n in sizes:
    test_activities = [
        (f"A{i}", i, i + 2)
        for i in range(n)
    ]

    result, elapsed, memory = measure_performance(
        activity_selection, test_activities
    )

    execution_times.append(elapsed)
    memory_usages.append(memory)

    print(
        f"Input Size: {n}, "
        f"Time: {elapsed:.6f} sec, "
        f"Peak Memory: {memory:.2f} KB"
    )


# Execution time graph
plt.figure(figsize=(8, 5))
plt.plot(sizes, execution_times, marker="o")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Activity Selection: Execution Time")
plt.grid(True)
plt.tight_layout()
plt.show()


# Memory usage graph
plt.figure(figsize=(8, 5))
plt.plot(sizes, memory_usages, marker="o")
plt.xlabel("Input Size (n)")
plt.ylabel("Peak Memory Usage (KB)")
plt.title("Activity Selection: Memory Usage")
plt.grid(True)
plt.tight_layout()
plt.show()

df = pd.DataFrame({
    "Input Size": sizes,
    "Execution Time (seconds)": execution_times,
    "Peak Memory (KB)": memory_usages
})

print("\nPerformance Comparison Table:")
print(df.to_string(index=False))

df.to_csv("greedy_performance.csv", index=False)
print("\nSaved results to greedy_performance.csv")
