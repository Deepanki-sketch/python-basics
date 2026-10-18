def Binary_Search():
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter array elements: ").split())) 
    target = int(input("Enter the target value: "))
    low = 0
    high = len(arr) -1
    while(low<=high):
        mid = (low + high) // 2
        if arr[mid]== target:
            return mid
        elif arr[mid]< target:
            low = mid +1
        elif arr[mid]> target:
            high = mid -1
        else:
            return -1
result = Binary_Search()        
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")    


    