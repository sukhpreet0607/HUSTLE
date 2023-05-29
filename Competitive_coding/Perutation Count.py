# def solve(A):
        
#         result = 0
#         l = []
#         for i in range(idx,-1,-1) :
#             l.append(A[i])
#             l.sort()
#             print (l)
#             if (l[-1]==len(l)) :
#                 result +=1
#         l=[]
#         print ("1st result : ",result)
#         for i in range(idx,len(A)) :
#             l.append(A[i])
#             l.sort()
#             print(l)
#             if (l[-1]==len(l)) :
#                 result +=1
#         return result

# print (solve([2,1,3,4]))


# import math
# def GCD (x,y) :
#     while (y) :
#         x,y = y,x%y
#     return abs(x)


# def solve(A, B):
#         gcd = []
#         while(len(B)>0) :
#             mx = 0
#             for j in range(1,len(B)) :
#                 gc  = math.gcd(B[0],B[j])
#                 if mx <=gc :
#                     mx  = gc
#                     idx = j
#             gcd.append(mx)
#             print (gcd,0,idx)
#             B.pop(0)
#             B.pop(idx-1)
#             print(B)
            
#         gcd.sort()
#         sum = 0
#         for i in range(0,A) :
#             sum += gcd[i]*(i+1)
#         return sum
            
# print (solve(3,[1,75,24,66,55,93]))



def xor (x,y) :
    res = 0
    for i in range(32) :
        if ((1<<i)&x != ((1<<y)&y)) :
            res |= 1<<i
    return res
    

def solve(A, B):
        res = []
        for query in B :
            k = 0
            for i in range(0,len(A)) :
                s=""
                for j in range(i,len(A)) :
                    s +=A[i]
                    xor_ans  = xor(int(s,base=2),query[0]) 
                    if xor_ans == query[1] :
                        k = 1
                        break
                if k==1 :
                    break
            if k==1 :
                res.append([i,j])
            else :
                res.append([-1,-1])
                
        return res

print (solve("100100010",[[2,6],[2,1]]))            

