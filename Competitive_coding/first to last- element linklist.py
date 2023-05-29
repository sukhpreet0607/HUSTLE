# Write a function that moves the last node to the front in a given Singly Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# Creating addNode() to add newly created nodes.
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

 # Creating display() to print newly created nodes via traversing.
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def mov(self):

        if self.head is None or self.head.next is None:
            pass
        else:
            s_last = self.head
            last = s_last.next

            while True:
                # print (s_last.data,last.data)
                if last.next == None :
                    last.next = self.head
                    s_last.next = None
                    self.head = last
                    break
                else :
                    s_last = last
                    last = last.next
        

s = SinglyLinkedList()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data = int(input('Enter data: '))
    s.addNode(data)
print('The linked list: ', end='')
s.display()
s.mov()
print ("")
s.display()
