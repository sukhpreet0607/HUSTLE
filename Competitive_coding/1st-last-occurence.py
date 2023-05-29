# First and last occurrences of x in sorted array
def find(arr,n,x):
    f = Fsearch(arr,0,n-1,x)
    print("First = ",f)
    l = Lsearch(arr,0,n-1,x)
    print("Last :",l)

def Fsearch(arr,left,right,x) :
    while left<right :
        mid = (left+right)//2
        if arr[mid]>=x:
            right = mid
        else :
            left = mid + 1
    return left

    

def Lsearch(arr,left,right,x) :
    while left<right :
        mid = (left+right)//2
        if arr[mid]<=x:
            left = mid
        else :
            right = mid - 1
    return left 


find([1,3,5,5,5,5,67,123,125],9,5)