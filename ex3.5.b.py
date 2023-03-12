import heapq
import timeit
import matplotlib.pyplot as plt

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

inefficient_times = []
efficient_times = []

# Measure the execution times for both functions and stores them
for i in range(1000):
    inefficient_time = timeit.timeit(lambda: inefficient(li[:i]), number=100)
    inefficient_times.append(inefficient_time)
    efficient_time = timeit.timeit(lambda: efficient(li[:i]), number=100)
    efficient_times.append(efficient_time)

# Print the aggregate (mean) of the measured values for each function
print("Inefficient Function - Mean: ", sum(inefficient_times)/len(inefficient_times), "seconds")
print("Efficient Function - Mean: ", sum(efficient_times)/len(efficient_times), "seconds")

# Plot the distribution of measured times using a histogram
fig, ax = plt.subplots()
ax.hist(inefficient_times, bins=50, alpha=0.5, label='Inefficient')
ax.hist(efficient_times, bins=50, alpha=0.5, label='Efficient')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Count')
ax.set_title('Distribution of Execution Times')
ax.legend()
plt.show()
