class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        res = 0
        for i in range (0,len(nums)-1) :
            product = nums[i]
            if product<k :
                res+=1
                
                for j in range (i+1,len(nums)):
                    product*=nums[j]
                    if product < k :
                        res+=1
                    else :
                        break
        if nums[len(nums)-1]<k :
            res+=1
        return resn