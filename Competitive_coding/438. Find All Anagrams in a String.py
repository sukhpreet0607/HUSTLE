def findAnagrams( s, p):
        result = []
        if len(p)>len(s) :
            return result
        i = 0

        while (i<=len(s)-len(p)) :
            subs = ''.join(sorted(s[i:i+len(p)]))
            # subs = []
            # subp= []
            # subs.extend(s[i:i+len(p)])
            # subp.extend(p)
            # subs.sort()
            # subp.sort()
            # print (subs,subp)

            if subs==subp:
                result.append(i)
            i+=1
        return result

print(findAnagrams("cbaebabacd","abc"))