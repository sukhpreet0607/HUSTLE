def findMinDiff(A,N,M):
        A.sort()
        # print(A)
        res = A[0:0+M][-1]-A[0:0+M][0] 
        
        for i in range(0,N-M+1):
            # print(A[i:i+M])
            if A[i:i+M][-1]-A[i:i+M][0] <= res:
                res = A[i:i+M][-1]-A[i:i+M][0]
            else :
                pass
        return res


print(findMinDiff([3, 4, 1 ,9 ,56, 7, 9 ,12],8,5))