import random
import time
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Radix Sort
def radix_sort(arr):
    def counting_sort(arr, exp):
        output = [0] * len(arr)
        count = [0] * 10
        for num in arr:
            count[(num // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = len(arr) - 1
        while i >= 0:
            idx = (arr[i] // exp) % 10
            output[count[idx] - 1] = arr[i]
            count[idx] -= 1
            i -= 1
        for i in range(len(arr)):
            arr[i] = output[i]

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Bucket Sort
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    for num in arr:
        index = int(num * n / 10000)
        buckets[index].append(num)
    for i in range(n):
        insertion_sort(buckets[i])
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Generate 1000 random integers between 1 and 10000
random_numbers = [random.randint(1, 10000) for _ in range(1000)]

# Function to measure execution time of sorting algorithms
def measure_sorting_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Measure the time taken for each sorting algorithm
bubble_time = measure_sorting_time(bubble_sort, random_numbers.copy())
insertion_time = measure_sorting_time(insertion_sort, random_numbers.copy())
merge_time = measure_sorting_time(merge_sort, random_numbers.copy())
selection_time = measure_sorting_time(selection_sort, random_numbers.copy())
radix_time = measure_sorting_time(radix_sort, random_numbers.copy())
bucket_time = measure_sorting_time(bucket_sort, random_numbers.copy())
quick_time = measure_sorting_time(lambda arr: quick_sort(arr), random_numbers.copy())

# Plotting
labels = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Selection Sort', 'Radix Sort', 'Bucket Sort', 'Quick Sort']
times = [bubble_time, insertion_time, merge_time, selection_time, radix_time, bucket_time, quick_time]

plt.bar(labels, times, color=['blue', 'orange', 'green', 'red', 'purple', 'pink', 'gray'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time Taken (seconds)')
plt.title('Time Taken by Sorting Algorithms')
plt.xticks(rotation=45)
plt.show()
