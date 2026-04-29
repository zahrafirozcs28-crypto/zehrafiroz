def find_previous_smaller_element(arr):
    n = len(arr)
    pse = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
            
        if stack:
            pse[i] = stack[-1]
            
        stack.append(arr[i])
        
    return pse

arr1 =
print(find_previous_smaller_element(arr1))

arr2 =
print(find_previous_smaller_element(arr2))
