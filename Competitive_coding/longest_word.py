# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:

# Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# Output: "apple"

def findLongestWord(s,dictionary):

    l = []

    for word in dictionary :

        # print (word)

        if  len(s)>=len(word) :
            temp = s
            i = 0  # i for temp
            j = 0  # j for word

            while i<len(word) and j<len(temp) :
              
                # print (i,j,temp[i],word[j],end=" :")

                if temp[i]==word[j] :
                    i +=1
                    j +=1

                else :
                    temp = temp[:i] + temp[i + 1:]
                
            
                # print (temp)
            
            temp = temp[:i]
            # print ("Final temp",temp)
            if temp==word :
                l.append(word)
            
    # print (l)
    ind = 0
    max_val = 0
    temp_l = []
    for i in range(0,len(l))  :
        
        if len(l[i]) > max_val :
            temp_l.clear()
            temp_l.append(l[i])
            max_val = len(l[i])

        elif len(l[i]) == max_val :
                temp_l.append(l[i])
        
        else :
            pass
    # print (min(temp_l))
            
    return min(temp_l)

        

print (findLongestWord("abpcplea",["ale","apple","monkey","plea","aplea"]))