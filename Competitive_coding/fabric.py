t = int(input())
test_cases = []

fabric_no = []

for i in range(1, t + 1):
    n = int(input())
    test = []
    for j in range(1, n+1):
        l = [ k for  k in input().split(" ")]
        test.append(l)
    
    
    test_cases.append(test)

# print (test_cases)


