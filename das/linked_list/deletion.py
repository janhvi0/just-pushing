class Node:
    def __init__(self, data):  # Corrected constructor
        self.data = data
        self.next = None

# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head of the linked list
head = node1

# Deleting node at the beginning
if head is not None:
    head = head.next
current = head
while current is not None:
    print(current.data, end=" --> ")
    current = current.next
print("None")


# Deleting node at the end
Current = head 
while Current.next.next is not None:
    Current = Current.next
Current.next=None

#deleting node at any perticular position

Current = head
while Current.next.next != 30:
    Current=Current.next
Current.next = Current.next.next