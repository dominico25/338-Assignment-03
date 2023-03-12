import json
import timeit
import matplotlib.pyplot as plt

def binary_search(arr, target, first_midpoint):
    start_idx = 0
    end_idx = len(arr) - 1
 
    if start_idx == 0:
        mid = first_midpoint
    else:
        mid = (start_idx + end_idx) // 2
    
    while start_idx <= end_idx:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start_idx = mid + 1
            mid = (start_idx + end_idx) // 2
        else:
            end_idx = mid - 1
            mid = (start_idx + end_idx) // 2

    return -1

with open("ex2data.json", "r") as json_file:
    data_array = json.load(json_file)

with open("ex2tasks.json", "r") as json_file:
    task_array = json.load(json_file)

times = []

# choose_mids is an array of 5 midpoint values. They are the start point of the array, 1/4 point of the array, 1/2 point of the array, 3/4 point of the array, and end of the array
choose_mids = [0, (len(data_array)-1) // 4, (len(data_array)-1) // 2, (len(data_array) - 1) - (len(data_array)-1) // 4, len(data_array)-1]

best_midpoints = []

for target in task_array:
    best_time = float('inf')
    best_midpoint = None
    for first_mid in choose_mids:
        time = timeit.timeit(lambda: binary_search(data_array, target, first_mid), number=1)
        if time < best_time:
            best_time = time
            best_midpoint = first_mid
    best_midpoints.append(best_midpoint)
    times.append(best_time)

plt.figure()
plt.scatter(task_array, best_midpoints)
plt.title("Tasks vs Corresponding Best Midpoint using Binary Search Method")
plt.xlabel("Task")
plt.ylabel("Best Midpoint")
plt.show()
