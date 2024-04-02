import heapq

def find_k_largest_elements(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
      
        if num > min_heap[0]:

            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
 
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result[::-1]

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 3
print("K largest elements:", find_k_largest_elements(nums, k))
