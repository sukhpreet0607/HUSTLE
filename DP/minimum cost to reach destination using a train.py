import sys

cost_arr = [[0, 15, 80, 90],
            [-1, 0, 40, 50],
            [-1, -1, 0, 70],
            [-1, -1, -1, 0]] 
              
# dp = [-1 for i in range(0,4)]

def cost(cost_arr,start,end,arr):
    mn_cost = sys.maxint
    if len(arr)==1 :
        return 
    # if dp[start]!=-1:
    #     return dp[i]    
    
    for i in range(start+1,end):
        mn_cost=min(mn_cost,cost(cost_arr,i,end,arr[i:]+cost_arr[start][i]  )
    
    dp[i]=mn_cost
    
    return mn_cost


print(cost(cost_arr,0,3,[1,2]))




# def minimum_cost_to_reach_destination(N, ticket_costs):
#     def dfs(station):
#         if station == N - 1:
#             return 0

#         min_cost = float('inf')

#         for next_station in range(station + 1, N):
#             min_cost = min(min_cost, ticket_costs[station][next_station] + dfs(next_station))

#         return min_cost

#     return dfs(0)

# # Example usage:
# N = 4
# ticket_costs = [[0, 15, 80, 90],
#                 [float('inf'),  0, 40, 50],
#                 [float('inf'), float('inf'), 0, 70],
#                 [float('inf'), float('inf'), float('inf'), 0]]

# print(minimum_cost_to_reach_destination(N, ticket_costs))  # Output: 65









