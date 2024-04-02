def sort_array_with_swapped_elements(arr):
    # Find the indices of the two elements that are not in their correct positions
    first_index, second_index = None, None
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if first_index is None:
                first_index = i
            else:
                second_index = i + 1
                break
    
    # Swap the two elements to restore the sorted order
    arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
    
    return arr

# Example:
arr = [1, 5, 3, 4, 2, 6]
sorted_arr = sort_array_with_swapped_elements(arr)
print("Sorted array:", sorted_arr)
