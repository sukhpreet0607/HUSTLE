t = int(input())
st = []
for i in range(1,t+1) :
    st.append(input())

D = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}

for string in st:
    num = []
    strList  = list(string)
    for i in D.keys():
        le = len(i)
        for j in i:
            try:
                if j in strList:
                    strList.remove(j)
                    le-=1
            except:
                pass
        if le == 0:
            num.append(D[i])
    num.sort()
    c = 0
    for k in num:
        if k==0:
            c+=1
    if c>0:
        num[0] = num[c]
        num[c] = 0
    s = ""
    print(s.join(num))
         







