def maximumMeetings(n,start,end):
    intervals = []
    for s,e in zip(start,end) :
        intervals.append([s,e])
    intervals.sort()
    # print (intervals)
    result = []
    result.append(intervals[0])
    for i in range(1,len(intervals)) : 
        if result[-1][1] > intervals[i][0] :
            if result[-1][1] < intervals[i][1] :
                pass
            elif result[-1][1] > intervals[i][1] :
                result.pop(-1)
                result.append(intervals[i])                
            else :
                if intervals[i][1]-intervals[i][0] > result[-1][1]-result[-1][0] :
                    pass
                else :
                    result.pop(-1)
                    result.append(intervals[i])
        else :
            result.append(intervals[i])
        # print (i,result)
    return ( len(result) )

print (maximumMeetings(8,[75250 ,50074 ,43659 ,8931 ,11273, 27545 ,50879 ,77924],[112960 ,114515 ,81825 ,93424 ,54316 ,35533 ,73383 ,160252]))      



# Input:
# N = 6
# start[] = {0,1,3,5,5,8}
# end[] =   {6,2,4,7,9,9}
# Output: 
# 4