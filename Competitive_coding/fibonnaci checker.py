class Solution(object):
    res = []
    def solve(self,st,arr,idx,n):

        if idx>=len(arr):
            return st
        
        for i in range(len(arr[idx])):
            st+=arr[idx][i]
            ans  = self.solve(st,arr,idx+1,n)
            if len(ans)==n:
                self.res.append(ans)
            st = st[:len(st)-1]
        
        return st

            


    def letterCombinations(self, digits):
        digs  = list(str(digits))
        n = len(digs)
        if n==0:
            return []
        print (digs)
        # tele  = {
        #     2 : ["a","b","c"],
        #     3 : ["d","e","f"],
        #     4 : ["g","h","i"],
        #     5 : ["j","k","l"],
        #     6 : ["m","n","o"],
        #     7 : ["p","q","r","s"],
        #     8 : ["t","u","v"],
        #     9 : ["w","x","y","z"]
        # }
        tele  = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        arr = []
        for i in digs:
            arr.append(tele[i])
        print (arr)
        self.solve("",arr,0,n)
        return self.res

obj = Solution()
print(obj.letterCombinations("234"))