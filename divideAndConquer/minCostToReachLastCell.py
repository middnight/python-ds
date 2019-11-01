"""
problem statement:-
1. we are given a 2D matrix.
2. accessing each cell has a cost assosiated with it.
3.we need to start from (0,0) and reach (n-1,n-1)
4. we can only go right or down cell from the current cell.
5. challenge is to do traversal in minimum cost.
"""

def calculate(matrix,row,column):
    list1=[]
    if(row<=-1  or column<= -1):
        return 1000000
    if(row==0 and column==0):
        return matrix[0][0]

    list1.append(calculate(matrix,row,column-1)+matrix[row][column])
    list1.append(calculate(matrix,row-1,column)+matrix[row][column])
    return min (list1)


matrix=[
    [4,7,8,6,4],
    [6,7,3,9,2],
    [3,8,1,2,4],
    [7,1,7,3,7],
    [2,9,8,9,3]
]
print(calculate(matrix,4,4))