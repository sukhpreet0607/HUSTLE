t = int(input())
test_cases = []

for i in range(1,t +1) :
   n = int(input())
   v_str =  [ int (i) for i in input().split(" ") ]
   v_str.insert(0,0) 
   test_cases.append(v_str) 


# print (test_cases)

for i in range(0,t) :

    for j in range(1,len(test_cases[i]) + 1)  :
        

