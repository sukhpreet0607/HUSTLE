def trappingWater(arr,n):
            sum=0
            l=[arr[0]]
            
            for i in range(1,n):
                if arr[i]>l[-1] :
                    l.append(arr[i])
                else :
                    l.append(l[-1])
            # print(l)

            arr.reverse()
            r=[arr[0]]
            for i in range(1,n):
                if arr[i]>r[-1] :
                    r.append(arr[i])
                else :
                    r.append(r[-1])
            r.reverse()
            # print(r)
            arr.reverse()

            for col in range(0,n):
                if l[col]>arr[col] and r[col]>arr[col] :
                    sum+=min(l[col],r[col])-arr[col]
                
            return sum

print ( trappingWater([7,4,0,9],4))