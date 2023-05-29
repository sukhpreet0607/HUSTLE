# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(strs) :
        ans = [[strs[0]]]
        for word in strs[1:] :
            # print (word, end=" ")
            k = 0
            for grp in ans :
                chk = 0
                if len(grp[0]) == len(word) :
                    s = grp[0]
                    for i in s :
                        if s.count(i) == word.count(i) :
                            chk +=1
                            s.replace(i,"")
                            word.replace(i,"")
                            
                    if chk==len(word) :
                        grp.append(word)
                        k +=1
                # print(grp)
               
            
            if k==0 :
                ans.append([word])
            
        print(ans)

groupAnagrams(["eat","tea","tan","ate","nat","bat"])  