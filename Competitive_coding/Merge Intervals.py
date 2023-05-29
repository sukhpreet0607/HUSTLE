def fnc(l) :
    return l[0]


def merge(intervals):
        i=0
        intervals.sort(key=fnc)
        while (i<len(intervals)-1) :
            if intervals[i+1][0] <= intervals[i][1] :
                l =[min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
                intervals[i] = l
                intervals.pop(i+1)
            else :
                i+=1
        return intervals


print(merge([[1,4],[0,0]]))