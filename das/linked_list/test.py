class createnode:
    def __init__(self,data):
        self.data=data
        self.next=None

# node1=createnode(300)
# node2=createnode(400)

# node1.next=node2

# print(node1.data)
# print(node1.next)
# print(node2.next)

class LinkedList:
    def __init__(self):
        self.head=None

    def insertBegin(self,Newdata):
        Newdata=createnode(Newdata)
        Newdata.nextdata=self.head
        self.head=Newdata

    def traversal(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            current=self.head
            while current is not None:
            # while current.next is not None:
            
                print(current.data,end="-->")
                current=current.next
            print("None")


    def insertEnd(self,Newdata):
        Newdata=createnode(Newdata)
        Newdata.nextdata=self.head
        self.head=Newdata
        if self.head is None:
            print("list is empty")
            return
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=Newdata
    



list1=LinkedList()
# list1.insertEnd(100)
# list1.insertEnd(200)
# list1.insertEnd(300)
# list1.insertEnd(400)
# list1.insertEnd(500)
list1.insertEnd(600)
list1.insertBegin(50)
print(list1.head.data)
# print(list1.traversal())





# list1=LinkedList()
# list1.insertBegin(100)
# list1.insertBegin(200)
# list1.insertBegin(300)
# list1.insertBegin(400)
# list1.insertBegin(500)
# print(list1.head.data)

