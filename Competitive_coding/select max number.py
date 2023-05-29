class Solution:
    def findDifferenceArray(self, N : int, A : List[int]) -> List[int]:
        i = 0
        result = []
        x = 0
        while(i<N) :
            if i==0:
                x=0
            elif i==1:
                x = A[0]
            else :
                if A[i-1]<=x :
                    x = A[i-1]
                    
            # l1 = [j for j in A[0:i]]
            l2 = [j for j in A[i+1:N]]
            # if len(l1)==0:
            #     x=0
            # else :
            #     x=min(l1)
                
            if len(l2)==0:
                y=0
            else :
                y=min(l2)
                
            result.append(x-y)
        return result