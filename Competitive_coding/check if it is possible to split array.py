class Solution:
    def canSplitArray(self, nums,m):
        if len(nums)==1 or len(nums)==2:
            return True
        
        arr1 = nums.copy()
        n = len(arr1)
        
        while (1):
            
            if n>=2 and sum(arr1)>=m:
                pass
            elif len(arr1)==1:
                return True
            else :
                return False
            
            if sum(arr1[0:n-1])>=sum(arr1[1:n]):
                arr1 = arr1[0:n-1]
            else:
                arr1 = arr1[1:n]
                
            if len(arr1)==1:
                return True
            n = len(arr1)

        return True
    
    
obj  = Solution()
print (obj.canSplitArray([4, 1, 3, 2, 4],6))