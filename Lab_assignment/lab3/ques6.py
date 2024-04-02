def has_pair_with_sum_quadratic(arr, K):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == K:
                return True
    return False

def has_pair_with_sum_linear(arr, K):
    arr.sort()
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == K:
            return True
        elif current_sum < K:
            left += 1
        else:
            right -= 1
    
    return False

# Example :
arr = [8, 4, 1, 6]
K = 10

print("Using O(n^2) algorithm:")
print("Pair with sum exists:", has_pair_with_sum_quadratic(arr, K))

print("\nUsing O(n log n) algorithm:")
print("Pair with sum exists:", has_pair_with_sum_linear(arr, K))
