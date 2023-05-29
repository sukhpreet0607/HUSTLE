class Solution(object):
    def largestGoodInteger(self,num):
        num_list = [int(i)  for i in num]
        res_list = []
        dig_list = []
        dig_list.append(num_list[0])
        for i in range(1,len(num_list)) :

            if len(dig_list)==1 and dig_list[0] == num_list[i] :
                dig_list.append(num_list[i])
            elif len(dig_list)==2 and dig_list[0] == num_list[i] and dig_list[1] == num_list[i] :
                dig_list.append(num_list[i])
                l = []
                for i in range(0,len(dig_list)) :
                    l.append(dig_list[i])
                res_list.append(l)
                dig_list.clear()
            else:
                dig_list.clear()
                dig_list.append(num_list[i])

        if len(res_list) == 0 :
            return ""

        elif len(res_list) == 1 :
            ans = ""
            for i in res_list :
                for j in i :
                    ans += str(j)

            return ans
        else :
            res_list.sort(reverse=True)
            return res_list[0]

print (largestGoodInteger("6777133339") )