
# bubble sort implementation 
def bubbleSort(arr):
    n= len(arr)
    
    # For loop to traverse through all
    # element in an array
    for i in range(n):
        for j in range(0, n-i-1):
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#defining the array to be used    
arr = [ 4, 1, 7, 3 ]
size=len(arr)
#calling the function bubble sort
bubbleSort(arr)
 
print("\nSorted array is:")
print(arr)
                
            