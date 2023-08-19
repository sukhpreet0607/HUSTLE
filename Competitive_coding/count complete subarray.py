class Solution:
    def countCompleteSubarrays(self, nums):
        res = 0
        
        dist = {}
        for i in range(len(nums)):
            if nums[i] not in dist:
                dist[nums[i]] = 1
            else :
                dist[nums[i]]+=1
        
        n = len(dist)
        # print(n)

        i = 0
        while(i<len(nums)):
            
            cnt = 0
            arr = []
            
            for j in range(i,len(nums)):
                # print (i,j," :",arr)
                if nums[j] not in arr:
                    cnt+=1
                    
                arr.append(nums[j])

                if cnt==n:
                    res+=1
                    res+= (len(nums)-j-1)
                    break

            i+=1
                
        return res

obj = Solution()
print(obj.countCompleteSubarrays([5,5,5,5]))          
                

  
                    
                
            