def miniMaxSum(arr):
    max_num = max(arr)
    min_num = min(arr)
    max_sum = 0
    min_sum = 0
    j = 0
    for i in arr :
        if i==max_num and j==0 :
            j +=1
            pass
        else:
            max_sum +=i
    
    j = 0
    for i in arr :
        if i==min_num and j==0 :
            j +=1
            pass
        else:
            min_sum +=i
    
    print (max_sum,min_sum)

miniMaxSum([1,3,5,7,9])


            
