from sys import maxsize

def solve(A):
        result = 0 
        if len(A)==3 :
            return A[0]+A[1]+A[2]
        sum= A[0]
        for i in range(1,len(A)-1):
            if sum <= (sum+A[i]) :
                
                sum +=A[i]
            else :
                break
        idx1 = i
        result  +=sum
        sum= A[-1]
        for i in range(len(A)-2,idx1+1,-1):
            if sum <= (sum+A[i]) :
                sum +=A[i]
            else :
                break
        result += sum
        idx3 = i
        
        far = -maxsize +1
        here =  0
        k = 0
        for i in range(idx1+1,idx3) :
            k+=1
            here +=A[i]
            if (far<here) :
                far = here
            if here<0 :
                here = 0
        if k > 0 :
            result += far
            return result
        else :
            return result
        
print (solve([27,27-66,-13,52,-56,-40]))