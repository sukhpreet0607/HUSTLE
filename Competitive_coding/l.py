class Solution(object):
    def digitSum(self,s, k):
        if ( len(s)<=k ) :
            return s
        else :
            j = 0
            str_sum = 0
            l = []
            for i in s :
                j+=1
                str_sum += int(i)
                if (j==k) :
                    j = 0
                    l.append(str_sum)
                    str_sum = 0
            if (j<k) :
                l.append(str_sum)
            s = ""
            for i in l :
                s+=str(i)
            
            return digitSum(self,s,k)
                        

# print (digitSum("11111222223",3))
