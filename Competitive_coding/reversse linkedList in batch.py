class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
#Creating addNode() to add newly created nodes.
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

 #Creating display() to print newly created nodes via traversing.
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
    
    def reverse(self,k):
        if (self.head.next==None):
            return self.head
        curr = head
        count = 0
        batch  = 0
        l = []
        while (curr!=None):
            count +=1
            if count <= k:
                
                if count ==1  :
                    l.append([curr])
                    prev=curr
                    curr =curr.next
                    prev.next = None
                    
                else:
                    next = curr.next
                    curr.next = prev
                    prev=curr
                    curr = next
                    
            elif batch==0:
                count = 0
                batch +=1
                head = prev
                # temp = prev
                # while (temp!=None):
                #     print(temp.data)
                #     temp = temp.next
            else :
                count = 0
                batch +=1
                l[-1].append[prev]
                
                # temp = prev
                # while (temp!=None):
                #     print(temp.data)
                #     temp = temp.next
            
        # print ("Batch",batch)
        # print (l)
        for i in range(1,len(l)) :
            l[i-1][0].next = l[i][1]
        return self.head
 
s = SinglyLinkedList()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data = int(input('Enter data: '))
    s.addNode(data)
print('The linked list: ', end = '')
s.display()
s.reverse(2)
s.display()