def subArrayExists(arr,n):
        d= {}
        pref = []
        sum = 0
        for i in range(0,n):
            if sum+arr[i]==0:
                return "Yes"
            else :
                sum+=arr[i]
                pref.append(sum)
            # print(pref)
            if sum in d.keys():
                return "Yes"
            else :
                d[sum]=1
            # print (d)
                    
        return "No" 

print(subArrayExists([1,2,3,4,5],5))