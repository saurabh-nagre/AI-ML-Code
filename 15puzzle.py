import copy
Target_list = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,'*']]

problem_list = [[1,2,3,4],
                [5,6,'*',8],
                [9,10,7,11],
                [13,14,15,12]]

#compares the updated list with target list and returns the h(x)
def comparator(list):

    hx = 0
    starCompared = 0

    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            if list[i][j]!=Target_list[i][j]:
                hx+=1
            if list[i][j]=='*' or Target_list[i][j]=='*':
                starCompared+=1
    
    if(starCompared>1):
        hx-=1
    return hx

#compares the optimised path and recursively calls for the optimised list
def solution(list,i,j,From,gx):
    optimised_fx = -1
    new_i = i
    new_j = j
    direction = None
    size = len(list)
    print("List at level ",gx,":",list)
    
    

    if From !='right' and j+1<size:
        new_list = copy.deepcopy(list)
        temp = new_list[i][j]
        new_list[i][j] = new_list[i][j+1]
        new_list[i][j+1] = temp
        hx = comparator(new_list)
        if hx==0:
            print("Target List Found:",new_list)
            return gx+1
        if optimised_fx==-1 or hx+gx<optimised_fx :
            optimised_fx = hx + gx
            new_i = i
            new_j = j+1
            direction = 'left'
            
    if From !='left' and j-1>=0:
        new_list = copy.deepcopy(list)
        temp = new_list[i][j]
        new_list[i][j] = new_list[i][j-1]
        new_list[i][j-1] = temp
        hx = comparator(new_list)
        if hx==0:
            print("Target List :",new_list)
            return gx+1
        if optimised_fx==-1 or hx+gx<optimised_fx:
            optimised_fx = hx + gx
            new_i = i
            new_j = j-1
            direction = 'right'

    if From !='top' and i-1>=0:
        new_list = copy.deepcopy(list)
        temp = new_list[i][j]
        new_list[i][j] = new_list[i-1][j]
        new_list[i-1][j] = temp
        hx = comparator(new_list)
        if hx==0:
            print("Target List :",new_list)
            return gx+1
        if optimised_fx==-1 or hx+gx<optimised_fx:
            optimised_fx = hx + gx
            new_i = i-1
            new_j = j
            direction = 'bottom'

    if From !='bottom' and i+1<size:
        new_list = copy.deepcopy(list)
        temp = new_list[i][j]
        new_list[i][j] = new_list[i+1][j]
        new_list[i+1][j] = temp
        hx = comparator(new_list)
        if hx==0:
            print("Target List :",new_list)
            return gx+1
        if optimised_fx==-1 or hx+gx<optimised_fx:
            optimised_fx = hx + gx
            new_i = i+1
            new_j = j
            direction = 'top'
    
    if new_i!=i or new_j!=j:
        temp = list[i][j]
        list[i][j] = list[new_i][new_j]
        list[new_i][new_j] = temp
        return solution(list,new_i,new_j,direction,gx+1)


row = 0
col = 0
for i in range(0,len(problem_list)):
    for j in range(0,len(problem_list[i])):
        if problem_list[i][j] =='*':
                row = i
                col = j
                break
    
print("Target Found at level", solution(problem_list,row,col,None,1))
    
