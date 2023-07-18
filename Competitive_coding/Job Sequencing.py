def p(x):
     return x[2]

def JobScheduling(Jobs,n):
        Jobs  = list(Jobs)
        mx=0
        for i in range(0,n) :
            mx = max(mx,Jobs[i][1])
        dead = [0]*(mx+1)
        # print (dead)
        prof = 0
        jdone = 0
        
        sorted(Jobs,key=p,reverse=True)
        print(Jobs)
        for i in range(0,n):
              if 0 in dead[1,Jobs[i][1]] :
                    
              
                 
                 

print(JobScheduling({(1,4,20),(2,1,10),(3,1,40),(4,1,30)},4))