t = int(input())
test_cases = []

for i in range(1,t +1) :
    x = int(input())
    test_cases.append(x)


def str_for (string,pos,ch) :
    return string[:pos] + str(ch) + string[pos:]

t = 1

for i in test_cases :
    l = []
    for j in range(len(str(i)),-1,-1) :
        for k in range(0,10) :
            if j==0 and k==0 :
                pass
            elif int(str_for(str(i),j,k)) % 9 ==0 :
                # print (int(str_for(str(i),j,k)))
                l.append(int(str_for(str(i),j,k)))
    l.sort()
    # print(l)
    print("Case #"+ str(t) +": "+ str(l[0]))
    t+=1