def KS(W, wt, val, n,dp):
    mx = 0 
 
    # Base Case
    if n == 0 or W == 0:
        return 0
    if dp[n-1][wt]!=-1:
        return dp[n-1][wt]
        
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        mx = KS(W, wt, val, n-1,dp)
        dp[n-1][wt] = mx
        return mx
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        mx  = max(val[n-1] + KS(W-wt[n-1], wt, val, n-1,dp),KS(W, wt, val, n-1,dp))
        dp[n-1][wt] = mx
        return mx 
            
dp = [[-1]*(4+1)]*3
# print(dp)
print (KS(4, [4,5,1], [1,2,3], 3,dp))