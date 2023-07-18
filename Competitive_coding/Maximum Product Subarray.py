def maxProduct(arr, n):
    mx = arr[0]
    for i in range(0, n):
            pro = arr[i]
            # print(pro,end=" ")
            for j in range(i+1, n):
                if pro*arr[j] > mx:
                    mx = pro*arr[j]
                pro *= arr[j]
                # print(pro,end=" ")
            # print(mx)
    return mx

print(maxProduct([6,-3,-10,0,2],5))