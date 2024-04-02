def max_product_pair(arr):
    if len(arr) < 2:
        return None
    
    max_num = arr[0]
    min_num = arr[0]
    max_product = arr[0] * arr[1]
    
    for num in arr[1:]:
        if num < 0:
            max_num, min_num = min_num, max_num
        
        max_num = max(num, max_num * num)
        min_num = min(num, min_num * num)
        
        max_product = max(max_product, max_num)
    
    return max_product

# Example :
arr = [-10, -3, 5, 6, -2]
product = max_product_pair(arr)
print("Maximum product:", product)
