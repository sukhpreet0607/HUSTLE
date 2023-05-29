t = int(input())
test_cases = []

for i in range(1,t +1) :
    I = input()
    P = input()
    t = (I,P)
    test_cases.append(t)

t = 1
for i in test_cases :
    if len(i[0]) > len(i[1]) :
        print ("Case #"+ str(t) +": "+ "IMPOSSIBLE" )

    elif len(i[0])==len(i[1]) :

        if (i[0]==i[1]) :
            print ("Case #"+ str(t) +": "+ "0")
        else :
            print ("Case #"+ str(t) +": "+ "IMPOSSIBLE" )

    else : 


        print ("Case #"+ str(t) +": " + str(len(i[1])-len(i[0])))