import random
import timeit

### Randomized Quicksort implementation
def randomized_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = randomized_partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

### Deterministic Quicksort implementation
def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = deterministic_partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

### Function to generate random arrays for testing
def generate_test_data(n):
    random_data = [random.randint(1, 10000) for _ in range(n)]
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted_data[::-1]
    repeated_data = [random_data[0]] * n
    return random_data, sorted_data, reverse_sorted_data, repeated_data

### Compare Randomized vs Deterministic Quicksort using timeit
def compare_using_timeit():
    test_sizes = [100, 1000, 5000]
    
    for n in test_sizes:
        random_data, sorted_data, reverse_sorted_data, repeated_data = generate_test_data(n)

        # Time Randomized Quicksort on different input types
        randomized_random_time = timeit.timeit(lambda: randomized_quicksort(random_data.copy()), number=10)
        randomized_sorted_time = timeit.timeit(lambda: randomized_quicksort(sorted_data.copy()), number=10)
        randomized_reverse_sorted_time = timeit.timeit(lambda: randomized_quicksort(reverse_sorted_data.copy()), number=10)
        randomized_repeated_time = timeit.timeit(lambda: randomized_quicksort(repeated_data.copy()), number=10)

       
        # Time Deterministic Quicksort on different input types
        deterministic_random_time = timeit.timeit(lambda: deterministic_quicksort(random_data.copy()), number=10)
        deterministic_sorted_time = timeit.timeit(lambda: deterministic_quicksort(sorted_data.copy()), number=10)
        deterministic_reverse_sorted_time = timeit.timeit(lambda: deterministic_quicksort(reverse_sorted_data.copy()), number=10)
        deterministic_repeated_time = timeit.timeit(lambda: deterministic_quicksort(repeated_data.copy()), number=10)

        # Print Format   
        print(f"\nArray Size: {n}")
        print(f"{'Array Type':<15} {'Randomized Time (s)':<25} {'Deterministic Time (s)'}")
        print(f"{'Random':<15} {randomized_random_time:<25.6f} {deterministic_random_time:.6f}")
        print(f"{'Sorted':<15} {randomized_sorted_time:<25.6f} {deterministic_sorted_time:.6f}")
        print(f"{'Reverse':<15} {randomized_reverse_sorted_time:<25.6f} {deterministic_reverse_sorted_time:.6f}")
        print(f"{'Repeated':<15} {randomized_repeated_time:<25.6f} {deterministic_repeated_time:.6f}")
# Run the comparison
compare_using_timeit()
