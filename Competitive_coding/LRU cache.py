#User function Template for python3

# design the class in the most optimal way

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        self.capacity = cap
        self.l  = []
        self.cache = {}
    
    def MoveKey(self,key):
        self.l.pop(key)
        self.l.append(key)
        
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        if key in self.l:
            # print(self.l)
            # print(self.cache)
            self.MoveKey(key)
            return self.cache[key]
        else :
            # print(self.l)
            # print(self.cache)
            return -1
            
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        if key in self.l:
            self.MoveKey(self,key)
            self.cache[key]=value
        else:
            if len(self.l)<self.capacity:
                self.l.append(key)
                self.cache[key]=value
            else:
                self.cache.pop(self.l[0])
                self.l.pop(0)
                self.l.append(key)
                self.cache[key]=value
        # print(self.l)
        # print(self.cache)



if __name__ == '__main__':
    # test_cases = int(input())
    # for cases in range(test_cases):
    cap = int(input())  # capacity of the cache
    qry=int(input())  #number of queries
    a = list(map(str, input().strip().split()))  # parent child info in list
        
    lru=LRUCache(cap)
        
       
    i=0
    q=1
    while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
    print()