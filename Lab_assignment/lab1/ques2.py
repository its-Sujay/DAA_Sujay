import random
import time
import matplotlib.pyplot as plt

# Function to perform linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Function to perform binary search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate an array of 10000 elements with random integers between 1 and 1000
arr = [random.randint(1, 1000) for _ in range(10000)]


def plot_search_times(search_function, search_name):
    search_times = []
    search_keys = [random.randint(1, 1000) for _ in range(5)]  # Generate 5 random search keys
    for key in search_keys:
        start_time = time.time()
        search_function(arr, key)
        end_time = time.time()
        search_times.append(end_time - start_time)
    plt.plot(search_keys, search_times, marker='o', label=search_name)


plot_search_times(linear_search, 'Linear Search')
plot_search_times(binary_search, 'Binary Search')
plt.xlabel('Search Key')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken by Linear and Binary Searches')
plt.legend()
plt.grid(True)
plt.show()
