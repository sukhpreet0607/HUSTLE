class Solution(object):
    def ambiguousCoordinates(self, s):
        print(s)
        n = len(s) - 2
        res = []
        i = 1

        x = 2
        while(i!=n):
            st1 = s[1:i+1]
            st2 = s[i+1:n-1]
            j = 1
            print ("st1:",st1,"st2:",st2)
            while (j!=len(st1)):
                # l = (list(st1)).insert(j,".")
                # st3  = "".join(l)
                st3 = st1[:j+1] + "." + st1[j:len(st1)]
                k  = 1
                
                while (k!=len(st2)):
                    # l = list(st2).insert(k,".")
                    # st4 = "".join(l)
                    st4 = st2[:k+1] + "." + st2[k:len(st2)]
                    print ("st3:",st3,"st4:",st4)
                    finSt = "({},{})"
                    res.append(finSt.format(st3,st4))
                    k+=1
                    st4 = st2[:len(st2)]
                st3 = st1[:len(st1)]
                j+=1
            i+=1
            x-=1
            if x==0 :
                break
        print (res)



obj = Solution()
print(obj.ambiguousCoordinates("(123)"))