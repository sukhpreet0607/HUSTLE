t = int(input())

test_cases = []
for i in range(1,t+1) :
    test_cases.append(int(input()))

def factors(x):
    l = []
    for i in range(1, x + 1) :
       if x % i == 0:
           l.append(i)
    return l   

t = 1 
for  i in test_cases :
    count = 0 
    fac = factors(i)
    for j in fac : 
        if str(j) == str(j)[::-1] :
            count +=1
    print ("Case #"+ str(t) +": " + str(count))
    t +=1

