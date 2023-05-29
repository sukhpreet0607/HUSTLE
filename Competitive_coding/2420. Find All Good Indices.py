class Solution(object):
    def goodIndices(self, nums, k):
        idx = [i for i in range(k,len(nums)-k)]
        n_idx = []
        if len(idx)==0 :
            # print (idx)
            return []
        else :
            # print (idx)
            for i in idx :
                # print(nums[i-k:i])
                # print (nums[i+1:i+k+1])
                if(nums[i-k:k] == sorted(nums[i-k:k],reverse=True) and nums[i+1:i+k+1] == sorted(nums[i+1:i+k+1])):
                    n_idx.append(i)
            # print (n_idx)
            return n_idx

obj = Solution()
print (obj.goodIndices([2,1,1,1,3,4,1],2))

