# SORTING ALGORITHMS AND FIBONACCI ALGORITHMS
# ============================================================


# ============================================================
# 1. BUBBLE SORT
# ============================================================

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# ============================================================
# 2. SELECTION SORT
# ============================================================

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ============================================================
# 3. INSERTION SORT
# ============================================================

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


# ============================================================
# 4. MERGE SORT
# ============================================================

def merge_sort(arr):

    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

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


# ============================================================
# 5. QUICK SORT
# ============================================================

def quick_sort(arr):

    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for x in arr:

        if x < pivot:
            left.append(x)

        elif x == pivot:
            middle.append(x)

        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


# ============================================================
# 6. FIBONACCI - RECURSIVE
# ============================================================

def fibonacci_recursive(n):

    if n <= 0:
        return 0

    if n == 1:
        return 1

    return (
        fibonacci_recursive(n - 1)
        + fibonacci_recursive(n - 2)
    )


# ============================================================
# 7. FIBONACCI - ITERATIVE
# ============================================================

def fibonacci_iterative(n):

    if n <= 0:
        return 0

    a = 0
    b = 1

    for i in range(n):

        a, b = b, a + b

    return a


# ============================================================
# 8. FIBONACCI - DYNAMIC PROGRAMMING
# ============================================================

def fibonacci_dynamic(n):

    if n <= 0:
        return 0

    if n == 1:
        return 1

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):

        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    # Test sorting algorithms
    numbers = [64, 25, 12, 22, 11, 90, 34]

    print("Original Array:")
    print(numbers)

    print("\nBubble Sort:")
    print(bubble_sort(numbers))

    print("\nSelection Sort:")
    print(selection_sort(numbers))

    print("\nInsertion Sort:")
    print(insertion_sort(numbers))

    print("\nMerge Sort:")
    print(merge_sort(numbers))

    print("\nQuick Sort:")
    print(quick_sort(numbers))


    # Test Fibonacci algorithms
    n = 10

    print("\n" + "=" * 40)
    print("FIBONACCI RESULTS")
    print("=" * 40)

    print("Recursive:", fibonacci_recursive(n))
    print("Iterative:", fibonacci_iterative(n))
    print("Dynamic Programming:", fibonacci_dynamic(n))
