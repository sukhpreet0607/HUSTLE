t = int(input())
l=[]

for i in range(1,t+1) :
    l.append(int(input()))

print ( l)

for i in range(0,t) :
    score = 0
    n = l[i]
    
    for j in range(1,n+1,4) :
        print (j)
        score = score + 1

    print ("Case #"+ str(i+1)+ ": " + str(score))