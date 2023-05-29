# class Solution(object):
def minimumCardPickup(cards):
    cards_arr = []
    cards_arr.append(cards[0])
    k = 0
    for i in range(1,len(cards)):
        for j in range(0,len(cards_arr)):
            if cards[i]==cards_arr[j] :
                k+=1
                return i - j + 1
        cards_arr.append(i)
    
    if k==0 :
        return -1
    
print (minimumCardPickup( [95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6] ))
             
        