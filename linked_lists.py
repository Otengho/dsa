
#create a linked list Node

class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

#a wrapper that wraps up all the Nodes
class LinkedLists:
    def __init__(self, head=None) -> None:
        self.head = head

#Inserting a Node in the List
    def inset_node(self, node):
        entry = ListNode(node)

        if self.head is None: #this implies that if the list is empty
            self.head = entry #insert data to the head
            return
        curr_node = self.head

        while True:
            if curr_node.next is None: #if the current Node is pointing to None
                curr_node.next = entry #instert the Data entry to next Node
                break
            curr_node = curr_node.next
        
    #Out putting the Linked lists
    def print_list(self):
        curr_node = self.head
        print("\nSingle Linked Lists\n-------------------")
        while curr_node != None:
            print(curr_node.data, end=" --> ") #print the data of the Node
            curr_node = curr_node.next #Move to the Next Node
        
        print("None") #Implies the last Node in the list points to None(No Node)

#Running the main program
if __name__ == "__main__":
    llist = LinkedLists() #creating an instance of the class Lisked Lists
    #inserting data to the List
    llist.inset_node(20)
    llist.inset_node(90)
    llist.inset_node(100)
    llist.inset_node(40)
    #displaying the list
    llist.print_list()