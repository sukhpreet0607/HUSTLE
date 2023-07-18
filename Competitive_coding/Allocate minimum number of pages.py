def findPages(A, N, M):
    size = N-M+1
    k = 1
    min = 0
    # for i in range(0,size):
    #     sum+=A[i]
    # min = sum
    # print(sum,end=" ")

    for s in range(size, 1, -1):
        sum = 0
        print(s, end=" ")
        
        for i in range(0, s):
            sum += A[i]
        print(sum, end=" ")

        if i==0 and k==1:
            min = sum
            k+=1
        elif sum<min:
            min = sum
        else :
            pass
        
        for j in range(0, N-s):
            sum -= A[j]
            sum += A[j+s]
            print(sum, end=" ")
            if sum <= min:
                min = sum
        print("\n")
    return min


print("Ans :", findPages([15, 10, 19, 10, 5, 18, 7], 7, 5))
