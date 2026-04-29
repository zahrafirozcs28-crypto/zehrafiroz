import heapq

def min_operations_to_half_sum(arr):
    initial_sum = sum(arr)
    target = initial_sum / 2
    current_sum = initial_sum
    
    max_heap = [-float(x) for x in arr]
    heapq.heapify(max_heap)
    
    ops = 0
    while current_sum > target:
        largest = -heapq.heappop(max_heap)
        reduction = largest / 2
        current_sum -= reduction
        heapq.heappush(max_heap, -reduction)
        ops += 1
        
    return ops

arr1 =
print(min_operations_to_half_sum(arr1))

arr2 =
print(min_operations_to_half_sum(arr2))
