from collections import Counter
 

def check(s1, s2):
   
    if(Counter(s1) == Counter(s2)):
        return 1
    else:
        return 0

def solve(input_str):
    n = len(input_str)

    dst = set()
    for i in range(n):
        dst.add(input_str[i])
    windLen = len(dst)
    i = 0
    j = windLen-1
    st= input_str[i:j+1]
    # sorted(st)

    x = 10

    while (len(st)!=len(input_str)):
        # print(input_str[i:j+1],st)
        if check(input_str[i:j+1],st):
            i+=windLen
            j+=windLen
            if j>=n:
                return st
        else:
            windLen+=1
            i=0
            j=windLen-1
            st = input_str[i:j+1]
        


    return input_str

# Example usage:
input_str = "bbaaababababaabb"
result = solve(input_str)
print(result)

input_str = "ababbaab"
result = solve(input_str)
print(result)

input_str = "abcbcacba"
result = solve(input_str)
print(result)












