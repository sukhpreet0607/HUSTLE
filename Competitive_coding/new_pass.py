import random
import string

t = int(input())

test_cases = []
for i in range(1,t+1) :
    l= []
    l.append(int(input()))
    l.append(input())
    test_cases.append(l)

t = 1 

for i in test_cases :
    checker = [0,0,0,0,0]
    if i[0]>=7 :
        checker[0] = 1
    for j in i[1] :
        if j.isupper() :
            checker[1] = 1
        elif j.islower() :
            checker[2] = 1
        elif j.isdigit() :
            checker[3] = 1
        elif j in ["*","&","#","@"] :
            checker[4] = 1

    while (1) :

        if sum(checker) >=4 and len(i[1])>=7 :
            break

        if checker[1] == 0:
            st = i[1]
            st += (random.choice(string.ascii_letters)).upper()
            i[1] = st
            # print (i[1])
            checker[1] = 1

        if checker[2] == 0 :
            st = i[1]
            st += (random.choice(string.ascii_letters)).lower()
            i[1] = st
            # print (i[1])
            checker[2] = 1
    
        if checker[3] == 0 :
            st = i[1]
            st += random.randint(0,9)
            i[1] = st
            # print (i[1])
            checker[3] = 1
    
        if checker[4] == 0 :
            st = i[1]
            st += random.choice(["*","&","#","@"])
            i[1] = st
            # print (i[1])
            checker[4] = 1

    print ("Case #"+ str(t) +": " + i[1])
    t += 1    
