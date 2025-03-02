# class Node:
#     def __init__(self, data):  # Corrected constructor
#         self.data = data
#         self.next = None

# # Creating nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)

# # Linking nodes
# node1.next = node2
# node2.next = node3
# node3.next = node4

# # Head of the linked list
# head = node1

# # Inserting new node at the beginning
# new_node = Node(50)
# new_node.next = head
# head = new_node  # Updating head to new node

# # Printing linked list
# current = head
# while current is not None:
#     print(current.data, end=" --> ")
#     current = current.next
# print("None")


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertNode(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,end="-->")
                current=current.next
            print("None")
    
    def insertAtBeginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insertAtEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node

    def insertAtPosition(self,data,position):
        new_node=Node(data)
        current=self.head
        while current is not None and current.data!= position:
            current=current.next

        new_node.next=current.next
        current.next=new_node



ll1=LinkedList()

ll1.insertNode(10)
ll1.insertNode(20)
ll1.insertNode(30)
ll1.insertNode(40)
ll1.insertNode(50)
ll1.insertAtEnd(5)
ll1.insertAtPosition(25,20)
ll1.printList()


