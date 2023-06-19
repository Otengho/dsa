

class Node:

	def __init__(self, data):
		## data of the node
		self.data = data

		## next pointer
		self.next = None

#create a Linked list
class LinkedList:

    def __init__(self) -> None:
        #initialize the head to None
        self.head = None

        #=====How to insert a Node to the Linked List=====.

        
        # If the head is empty, then assign the new node to the head.
        # If the head is not empty, get the last node of the linked list.
        # Assign the new node to the last node next pointer.

    def insert(self, new_node):

        if self.head:
            last_node = self.head
            while last_node != None:
                last_node = last_node.next
            
            last_node = new_node
    
        else: 
            # Check whether the head is empty or not.
            ## assigning the node to head
            last_node = self.head


    def display(self):
            ## variable for iteration
            temp_node = self.head

            ## iterating until we reach the end of the linked list
            while temp_node != None:
                ## printing the node data
                print(temp_node.data, end='->')

                ## moving to the next node
                temp_node = temp_node.next

            print('Null')



if __name__ == '__main__':
	## instantiating the linked list
	linked_list = LinkedList()

	## inserting the data into the linked list
	linked_list.insert(Node(1))

	## printing the linked list
	linked_list.display()