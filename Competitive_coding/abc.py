class Solution(object):
  def largestInteger(self, num):
   if (num>=1 and num<= 10000000000):

    num_arr = [int(a) for a in str(num)]
    num_arr.reverse()
    len_arr = len(num_arr)
    mi  = 0
    ind = 0
    for i in range(1,len_arr + 1) :
        x = 0
    
        if (i%2!=0) :
         for j in range(i + 1, len_arr + 1) :
            if (j%2!=0) :
                if (num_arr[j-1]<num_arr[i-1]) :
                    mi = num_arr[j - 1]
                    ind = j-1
                    x +=1

         if (x > 0) :
            temp = num_arr[i-1]
            num_arr[i-1] = mi
            num_arr[ind] = temp        
                    
        else :
         for j in range(i + 1, len_arr + 1) :
            if (j%2==0) :
                if (num_arr[j-1]<num_arr[i-1]) :
                    mi = num_arr[j - 1]
                    ind = j-1
                    x +=1
        
         if (x > 0) :
            temp = num_arr[i-1]
            num_arr[i-1] = mi
            num_arr[ind] = temp

    num_arr.reverse()
    largest = ""
    for  i in num_arr :
        largest += str(i)
    
    return int(largest)

obj = Solution()
print (obj.largestInteger(247))


