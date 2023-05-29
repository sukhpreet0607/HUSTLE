from typing import List

class Solution:
    def minimumTime(self, N : int, NUM : int, time : List[int]) -> int:
        i = 0
        
        while(1):
            count = 0
            for k in time:
                count+=i//k
                if count>=NUM :
                    return i
            i+=1
                