"""
problem statement- 
1. we are given a 2D matrix.
2. Accessing each cell have a cost assossiated with it.
3. we need to start from (0,0) cell and go till (n-1,n-1) cell.
4. we are given total cost to reach the last cell.
5. challenge is to find the total number of ways to reach the end of the matrix in given total cost.


"""

def calculate(array,row,col,cost):

    if(cost<0):
        return 0
    
    if(row==0 and col==0):
        if(cost-array[row][col]==0):
            return 1
        else:
            return 0


    if(row==0):
        return calculate(array,0,col-1,cost-array[row][col])
    if(col==0):
        return calculate(array,row-1,0,cost-array[row][col])

        

    numberOfWaysFromRows= calculate(array,row-1,col,cost-array[row][col])
    numberOfWaysFromCols= calculate(array,row,col-1,cost-array[row][col])
    
    return numberOfWaysFromCols+numberOfWaysFromRows


array=[
    [4,7,1,6],
    [5,7,3,9],
    [3,2,1,2],
    [7,1,6,3],
    ]

print(calculate(array,3,3,20))