class Solution(object):
    def maxSum(self, nums):
        n = len(nums)
        maxDig = []
        for i in nums:
            maxDig.append( max(list( str(i) ) ) )
                          
        print(maxDig)
        

obj = Solution()
print(obj.maxSum([51,71,17,24,42]))