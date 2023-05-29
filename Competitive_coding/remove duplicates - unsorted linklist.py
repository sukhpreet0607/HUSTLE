#  Brute force approach
def Duplicates(head):
        node = head
        
        while (node!=None) :
            temp  = node.next
            prev = node
            while (temp!=None) :
                if (node.data == temp.data) :
                    prev.next = temp.next
                    temp = prev.next
                    
                else :
                    prev = temp
                    temp = temp.next
                 
            node = node.next
        return head



// Hashing

def removeDuplicates(self, head):
        node = head
        counter = []
        counter.append(node.data)
        prev = node
        node = node.next
        while (node!=None) :
            if node.data not in counter :
                counter.append(node.data)
                prev = node
                node = node.next
            else :
                prev.next = node.next
                node = node.next
                
        return head
