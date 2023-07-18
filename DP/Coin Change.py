# This is brute force recursion approach . As it calculates all the possible combinations , 
# it also calculates some repetitive combinations sio it will give wrong ans



def func(arr,n,Sum):
        res  = 0
        for i in range(0,n):
            if Sum==0:
                return 1
            elif Sum<0:
                return 0
            else:
                res+=func(arr,n,Sum-arr[i])
        return res 
        
# now this is the modified approach for the func method
def func1(arr, n, Sum,index):
        if Sum == 0:
            return 1
        elif Sum < 0:
            return 0
        
        res = 0
        for i in range(index, n):
            res += func1(arr, n, Sum - arr[i], i)
            
        return res
        
        
        
def count( coins, N, Sum):
        return func1(coins,N,Sum,0)

print(count([1,2,3],3,4))