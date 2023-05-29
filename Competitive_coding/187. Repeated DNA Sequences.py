def findRepeatedDnaSequences(s):
    result = set(())
    if len(s) <10 :
        return result

    for i in range(0,len(s)) :
        if len(s[i:i+10]) <10 :
            return result
        else :
            sub = s[i:i+10]
            if s.find(sub,i+1) >=0 :
                result.add(sub)



print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))


