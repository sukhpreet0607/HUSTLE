import  math
t = int(input())

test_cases = []
for i in range(1,t+1) :
    l = [int(j) for j in input().split(" ")]
    test_cases.append(l) 

t = 1
for i in test_cases :
    r = i[0]
    sum_sq_r = 0
    j = 1
    while (r>=1) :
        sum_sq_r += (r**2)
        if (j%2)!=0 :
            r *= i[1]
            j += 1
        else:
            r /= i[2]
            j +=1

    print ("Case #"+ str(t) +": " + str(round((math.pi)*sum_sq_r,12)) )
    # print ("Case #"+ str(t) +": " + str((math.pi)*sum_sq_r))

    t+=1
            