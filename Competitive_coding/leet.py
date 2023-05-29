class Solution(object):
    def findClosestnumsber(self,nums):
        arr_list = [] 
        n = len(nums)
        min = abs(nums[0])
        for i in range(1,n) :
            if (abs(nums[i]) < min) :
                min = abs(nums[i])
                # re_list[0] = min
                ind = i
        
        for i in range(0,n) :
            if (abs(nums[ind]) == abs(nums[i])) :
                arr_list.append(i)

        if (len(arr_list)==1) :
            return nums[ind]

        max = nums[arr_list[0]]
        
        for i in range(1,len(arr_list)) :
            if (nums[arr_list[i]] > max ) :
                max = nums[arr_list[i]]
        return max





# nums = [-4,-2,1,4,-1,8]

# print (findClosestnumsber(nums))

            
