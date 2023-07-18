def findLongestConseqSubseq(arr, N):
        arr.sort()
        # print(arr)
        mx = 1
        l = 1
        for i in range(1,N):
            if arr[i]-arr[i-1]==1:
                l+=1
                mx = max(mx,l)
            else :
                l=1
            # print(mx,end=" ")

        return mx

print(findLongestConseqSubseq([2,0,1,1,4],5))