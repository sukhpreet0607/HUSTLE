def generateMatrix(n):
    top,rigth,bottom,left = 0,n-1,n-1,0
    row,col, = 0,0
    # print (top,rigth,bottom,left)
    result = [[0]*n for i in range(0,n)]
    # print (result)
    n *=n
    i=1

    while (i<=n) :

        if row == top and col<=rigth: 
            if col==rigth :
                top +=1
            else :
                result[row][col] = i
                col += 1

        elif col==rigth and row<=bottom:
            if row==bottom:
                rigth -=1
            else :
                result[row][col] = i
                row +=1

        elif row==bottom and col>=left:
            if col==left:
                bottom +=1
            else :
                result[row][col] = i
                col -=1

        elif col==left and row>=top:
            if row==top:
                left +=1
            else :
                result[row][col] = i
                row -=1
        else :
            pass

        print (i, result)
        i +=1

    return result

matrix = generateMatrix(3)
n=3

for row in range(0,n):
    for column in range(0,n):
        print(matrix[row][column], end=" ")
    print()

