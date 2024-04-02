import heapq

def print_sorted_lists(lists):
    min_heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i))
            lists[i] = lst[1:]  
    
    while min_heap:
        element, list_index = heapq.heappop(min_heap)
        print(element, end=' ')
        if lists[list_index]:
            heapq.heappush(min_heap, (lists[list_index][0], list_index))
            lists[list_index] = lists[list_index][1:]  # Move to the next element of the list


lists = [
    [1, 3, 5],
    [2, 4, 6],
    [0, 7, 8]
]

print_sorted_lists(lists)
