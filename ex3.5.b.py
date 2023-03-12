import heapq
import timeit
import statistics

def inefficient(li):
    heap = []
    for i in range(len(li)):
        if li[i] > 5:
            heapq.heappush(heap, -li[i])
        else:
            if heap:
                li[i] = -heapq.heappop(heap)
            else:
                li[i] = None
    while heap:
        li.append(-heapq.heappop(heap))

def efficient(li, heap=None):
    if heap is None:
        heap = []
    for i in range(len(li)):
        if li[i] > 5:
            heapq.heappush(heap, -li[i])
        else:
            if heap:
                li[i] = -heapq.heappop(heap)
            else:
                li[i] = None
    while heap:
        li.append(-heapq.heappop(heap))
    return heap

# Generate a list of at least 1000 elements
li = list(range(1000))

# Initialize lists to store the measured times
inefficient_times = []
efficient_times = []

# Measure the execution times for both functions and store them in the corresponding lists
for i in range(1000):
    inefficient_time = timeit.timeit(lambda: inefficient(li[:i]), number=100)
    inefficient_times.append(inefficient_time)
    efficient_time = timeit.timeit(lambda: efficient(li[:i]), number=100)
    efficient_times.append(efficient_time)

# Print the aggregate (mean) of the measured times for both functions
print(f'Inefficient function - Mean: {statistics.mean(inefficient_times)}')
print(f'Efficient function - Mean: {statistics.mean(efficient_times)}')

