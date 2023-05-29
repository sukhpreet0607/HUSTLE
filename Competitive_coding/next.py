t = int(input())
lt=[]

for i in range(1,t+1) :
    n = int(input())
    l = input().split(" ")
    lt.append(l)


for j in range(0,t) :
    n = len(lt[j])
    
    print ("Case #"+ str(j+1)+ ": ",end="")   

    for i in range(0,n) :
        mentor = -1
        student = lt[j][i]
        l=[]

        for k in range(0,n) :
            ment = lt[j][k]
            if ( i!=k and ment <= 2*student) :
                l.append(ment)

        # print ("max list :",l)

        if (len(l) != 0) :
            mentor = max(l)
        print (mentor,end=" ")
    print("")
    
    

