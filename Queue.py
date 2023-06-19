#queue follows the FIFO methodology
#the fisrt element to be input comes out first

#declaring an empty queue
queue = []
  
# Adding elements to the queue by appending them to the above empty queue
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
queue.append('e')
#printing the Queue before any operation
print("Initial queue")
print(queue)
  
# Removing 3 elements from the queue and print them out
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
#Printing elements left in a queue
print("\nQueue after removing elements")
print(queue)
