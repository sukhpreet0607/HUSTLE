class solution:
    def longestPalindrome(self, s):
        n = len(s)
        maxLen = 1
        start,end= 0,0
        for i in range(1,n):
            len1 = self.Palindrome(s,i,i,n)
            len2 = self.Plaindrome(s,i,i+1,n)
            Len = max(len1,len2)
            if Len>maxLen :
                if Len%2!=0:
                    start = i - Len//2 
                    end  = i + Len//2
                else :
                    start = i - (Len)//2 + 1
                    end  = i + Len//2
        return s[start:end+1]
    
    
    def Palindrome(self,s,i,j,n):
        while(i>=0 and j<n):
            if s[i]!=s[j]:
                break
            i-=1
            j+=1
        return j-i+1

        
obj  = solution()
print (obj.longestPalindrome("aaaabbaa"))