import time
import tracemalloc

def activity_selection(activities):
    #sort activities by finishing time
    activities = sorted(activities, key = lambda x:x[1])

    selected = []
    last_finish_time = -1

    for start, finish in activities:
        if start >= last_finish_time:
            selected.append((start, finish))
            last_finish_time = finish

    return selected 

def measure_performance(algorithm, *args):
    #Measure execution time
    tracemalloc.start()
    start_time = time.perf_counter()

    result = algorithm(*args)

    end_time = time.perf_counter()

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_usage = peak_memory / 1024 #convert bytes to KB

    return{
        "result": result,
        "execution_time_seconds": execution_time,
        "peak_memory_kb": memory_usage
    }

activities = [
    (1,3),
    (2,5),
    (4,6),
    (6,8),
    (5,7),
    (8,9)
]

#Example activity_Selection is your implemented function
stats = measure_performance(activity_selection,activities)

print("Result: ", stats["result"])
print("Executable Time: ", stats["execution_time_seconds"],"seconds")
print("Peak Memory: ", stats["peak_memory_kb"], "KB")
