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

# # Inserting new node at the end
# new_node = Node(50)
# new_node.next = None
# node4.next = new_node

# Printing linked list
current = head
# while current is not None:
#     print(current.data, end=" --> ")
#     current = current.next
# print("None")

# print(node4.next)


#insert at any perticular position lest say at 3nd position after 20
new_node = Node(25)
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node
print(current.data)

