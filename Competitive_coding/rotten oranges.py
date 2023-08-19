def orangesRotting(self, grid):
	count = 0
	while (1):
		flag = 0
		l = []
		for i in range(len(grid)):
		    for j in range(len(grid[0])):
		            if grid[i][j] == 2 and (i, j) not in l:
		                if grid[i-1][j] == 1:
		                    grid[i-1][j] = 2
				            l.append((i-1, j))
		                    flag += 1
		                if grid[i+1][j] == 1:
		                    grid[i+1][j] = 2
		                    l.append((i+1, j))
		                    flag += 1
		                if grid[i][j-1] == 1:
		                    grid[i][j-1] = 2
		                    l.append((i, j-1))
		                    flag += 1
		                if grid[i][j+1] == 1:
		                    grid[i][j+1] = 2
		                    l.append((i, j+1))
		                    flag += 1
		                else:
		                    pass
		   l=[]
		   if flag>0:
		       count+=1
		   else :
		       break
		   
		 for i in range(len(grid)):
		        for j in range(len(grid[0])):
		            if grid[i][j]==1:
		                return -1
		            else :
		                pass
		    
		return count