
#Selection Sort
#defining the selection sort function
def selectionSort(array, size):
    for s in range (size):
        min_idx = s
        for i in range(s+1, size):
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
                 # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])
        
#defining the array to be used
data = [7, 2, 1, 6 ]
size = len(data)
#calling the selection sort function and passing in the array and
#array size
selectionSort(data, size)
#displaying sorted array "data" in ascending order
print('\nSeletion Sort is:\n------------------')
print(data)


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
arr = [2, 23, 10, 1]
size=len(arr)
#calling the function bubble sort
bubbleSort(arr)
 
print("\nBubble Sort is:\n-----------------")
print(arr)

#defining the insertion sort function
def insertion_sort(_array):

		# Outer loop to traverse on len(array)
		for i in range(1, len(_array)):
			a = _array[i]

			# Move elements of array from 0 to i-1,
			j = i - 1
			while j >= 0 and a < _array[j]:
				_array[j + 1] = _array[j]
				j -= 1
				
			_array[j + 1] = a
			
		return _array
			
#defining an array 
arr = [ 7, 2, 1, 6 ]
print("\nInsertion Sort is:\n-----------------")
print(insertion_sort(arr))




