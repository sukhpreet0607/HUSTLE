def minSwaps(nums):
    res = 0
    sort_nums = nums.copy()
    sort_nums.sort()
    l = {}
    for i in range(len(sort_nums)):
        l[sort_nums[i]] = i
    # print(l)
    # print (nums)
    i = 0
    n = len(nums)
    while (i < n):
        # print(i,l[nums[i]])
        if l[nums[i]] != i:
            temp = nums[l[nums[i]]]
            nums[l[nums[i]]] = nums[i]
            nums[i] = temp
            res += 1
        else:
            i += 1
        # print(res)
    return res

print(minSwaps([2,8,5,4]))
