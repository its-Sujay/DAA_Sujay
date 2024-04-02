def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, inv_left = merge_sort(arr[:mid])
    right_half, inv_right = merge_sort(arr[mid:])
    
    merged_arr, inversions = merge(left_half, right_half)
    
    return merged_arr, inv_left + inv_right + inversions

def merge(left, right):
    merged = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i  # Count inversions
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inversions

# Example :
A = [10, 1, 2, 4, 13, 9, 5]
sorted_A, inv_count = merge_sort(A)
print("Sorted array:", sorted_A)
print("Inversion count:", inv_count)
