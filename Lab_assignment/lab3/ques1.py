def find_pair_with_sum(arr, target_sum):
    num_indices = {}
    
    for i, num in enumerate(arr):
        diff = target_sum - num
        if diff in num_indices:
            return [num_indices[diff], i]
        num_indices[num] = i
    
    return None

# Example usage:
arr = [1, 3, 5, 7, 9]
target_sum = 8
pair_indices = find_pair_with_sum(arr, target_sum)

if pair_indices:
    print(f"Pair with sum {target_sum} found at indices:", pair_indices)
    print("Pair:", arr[pair_indices[0]], arr[pair_indices[1]])
else:
    print("No pair found with the given sum.")
