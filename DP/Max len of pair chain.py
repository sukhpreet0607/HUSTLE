import sys
class Solution(object):

    def solve(self,pairs,prev,idx):
        self.x+=1
        ans = 0
        # print ("Call :",self.x,prev,pairs)
        if idx==len(pairs):
            return 0

        for i in range(idx,len(pairs)):
            if prev[1]<pairs[i][0]:
                prev = [pairs[i][0],pairs[i][1]]
                ans = max(ans,1 + self.solve(pairs,prev,i+1))
            else : 
                ans = max(ans,0 + self.solve(pairs,prev,i+1))
        return ans


    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x: x[1])
        # print(pairs)
        prev = [-2000,-2000]
        return self.solve(pairs,prev,0)
      
obj = Solution()
print(obj.findLongestChain([[1,2],[7,8],[4,5]]))