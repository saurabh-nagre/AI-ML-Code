import sys
import copy
int_max = sys.maxsize #for infinity
# original matrix
matrix =   [[int_max,10,5,3],
            [8,int_max,9,7],
            [1,6,int_max,9],
            [2,3,8,int_max]]


#finds the reduced cost of matrix
def reduction(matrix):
    reduction_sum = 0
    length = len(matrix)
    # row reduction
    for i in range(0,length):
        min = int_max
        for j in range(0,length):
            if min>matrix[i][j]:
                min = matrix[i][j]
        
        if min==int_max:
            min = 0
        reduction_sum+=min
        if min!=0:
            for j in range(0,length):
                if matrix[i][j]!=int_max:
                    matrix[i][j]-=min
                if matrix[i][j]<0:
                    matrix[i][j] = 0
    # column reduction
    for i in range(0,length):
        min = matrix[0][i]
        for j in range(1,length):
            if min>matrix[j][i]:
                min = matrix[j][i]
        if min==int_max:
            min = 0
        reduction_sum+=min
        if min!=0:
            for j in range(0,length):
                if matrix[j][i]!=int_max:
                    matrix[j][i]-=min
                if matrix[j][i]<0:
                    matrix[j][i] = 0
    return reduction_sum
# Minimum cost of path
min_cost_path = reduction(matrix)



# finMinPath for finding the next node of path which gives #less cost
def findMinPath(matrix,path,path_cost):

    print(path," cost = ",path_cost)
    index = -1 #index of new node
    min_cost = int_max #min cost to reach next node
    min_matrix = None  #matrix to pass on to next function
    for col in range(1,len(matrix)):
        if col not in path:
            mat = copy.deepcopy(matrix)
            for i in range(0,len(mat)):
      	# row of last node and col of next node made infinify
                mat[i][col] = int_max
                mat[path[-1]][i] = int_max
            for i in path:
                mat[col][i] = int_max

            cost = path_cost + reduction(mat) + matrix[path[-1]][col]
            print(col,":",cost,end = " ")
            if min_cost>cost:
                min_cost = cost
                index = col
                min_matrix = copy.deepcopy(mat)
    print("")
   
    if index!=-1:
        path.append(index)
        return findMinPath(min_matrix,path,min_cost)
    else:
        path.append(1)
        min_cost = 0 + path_cost
        return min_cost        

path = [0]
final_cost =findMinPath(matrix,path,min_cost_path)+matrix[path[-2]][0]

print("final path:",path)
print("final cost:",final_cost)
