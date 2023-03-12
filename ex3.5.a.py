import random
import timeit
import matplotlib.pyplot as plt

def inefficient_search(li, target):
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1

def efficient_search(li, target):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Creates a sorted array of 2000 random integer elements in the range of 0-10000
initial_array = [random.randint(0, 10000) for _ in range(2000)]
initial_array.sort()

# Number of measurements to be taken
num_measurements = 100

# Lists to store the measured values
inefficient_search_times = []
efficient_search_times = []

# Measure execution times
for i in range(num_measurements):
    inefficient_search_time = timeit.timeit(lambda: inefficient_search(initial_array, 5000), number=1000)
    efficient_search_time = timeit.timeit(lambda: efficient_search(initial_array, 5000), number=1000)
    inefficient_search_times.append(inefficient_search_time)
    efficient_search_times.append(efficient_search_time)

# Printing aggregate of measured values for inefficient and efficient (Prints both min and avg time)
print(f"Inefficient Search:\nMinimum: {min(inefficient_search_times)} seconds\nAverage: {sum(inefficient_search_times)/len(inefficient_search_times)} seconds\n")
print(f"Efficient Search:\nMinimum: {min(efficient_search_times)} seconds\nAverage: {sum(efficient_search_times)/len(efficient_search_times)} seconds\n")

# Plotting distribution of measured values
plt.hist(inefficient_search_times, alpha=0.5, label='Inefficient Search')
plt.hist(efficient_search_times, alpha=0.5, label='Efficient Search')
plt.legend(loc='upper right')
plt.title(f"Execution Time Distribution ({num_measurements} measurements)")
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.show()





