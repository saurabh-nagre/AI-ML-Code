import copy
import sys

maxInt = sys.maxsize
minInt = sys.maxsize*-1

def checkWinner(board):
    for i in range(0,3):
        if board[i][0]=='x' and board[i][1]=='x' and board[i][2]=='x':
            return 1
        if board[i][0]=='o' and board[i][1]=='o' and board[i][2]=='o':
            return -1
        if board[0][i]=='x' and board[1][i]=='x' and board[2][i]=='x':
            return 1
        if board[0][i]=='o' and board[1][i]=='o' and board[2][i]=='o':
            return -1
    
    if board[0][0]=='x' and board[1][1]=='x' and board[2][2]=='x':
            return 1
    elif board[0][2]=='x' and board[1][1]=='x' and board[2][0] == 'x':
        return 1
    elif board[0][2]=='o' and board[1][1]=='o' and board[2][0] == 'o':
        return -1
    elif board[0][0]=='o' and board[1][1]=='o' and board[2][2]=='o':
            return -1
    else: return 0
               
def isterminal(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==''):
                return 1

    return 0             

def minimax(board,x,y,depth,ismaximiser):
    if(ismaximiser==True):
        board[x][y] = 'x' #maximizer
        bestmove = {'depth':maxInt,'score':minInt}
    else: 
        board[x][y] = 'o' #minimizer
        bestmove = {'depth':maxInt,'score':maxInt}

    winner = checkWinner(board)
    if winner!=0:
        bestmove['depth'] = depth
        bestmove['score'] = winner
        return bestmove
    else:
        toContinue = isterminal(board)
        if toContinue==0:
            bestmove['depth'] = depth
            bestmove['score'] = 0
            return bestmove
        if ismaximiser==True:       
                for i in range(0,3):
                    for j in range(0,3):
                        if(board[i][j]==''):
                            p = copy.deepcopy(board)
                            move = minimax(p,i,j,depth+1,not ismaximiser)
                            if move.get('score')>bestmove.get('score'):
                               bestmove['depth'] = move.get('depth')
                               bestmove['score'] = move.get('score')
                            elif move.get('score')==bestmove.get('score') and move.get('depth')<bestmove.get('depth'):
                                bestmove['depth'] = move.get('depth')
                                bestmove['score'] = move.get('score')
                return bestmove
        else:
            for i in range(0,3):
                    for j in range(0,3):
                        if(board[i][j]==''):
                            p = copy.deepcopy(board)
                            move = minimax(p,i,j,depth+1,not ismaximiser)
                            if move.get('score')<bestmove.get('score'):
                                bestmove['depth'] = move.get('depth')
                                bestmove['score'] = move.get('score')
                            elif move.get('score')==bestmove.get('score') and move.get('depth')<bestmove.get('depth'):
                                bestmove['depth'] = move.get('depth')
                                bestmove['score'] = move.get('score')
            return bestmove

board = [['x','o','o'],
         ['','x','o'],
         ['x','o','']]
bestmove = {'x':-1,'y':-1,'depth':maxInt,'score':minInt}

player = True

for i in range(0,3):
    for j in range(0,3):
        if board[i][j]=='':
            p = copy.deepcopy(board)
            move = minimax(p,i,j,1,player)
            if player==True:
                if move.get('score')>bestmove.get('score') or move.get('score')==bestmove.get('score') and move.get('depth')<bestmove.get('depth'):
                    bestmove['score'] = move.get('score') 
                    bestmove['x'] = i
                    bestmove['y'] = j
                    bestmove['depth'] = move.get('depth')
            else:
                if move.get('score')>bestmove.get('score') or move.get('score')==bestmove.get('score') and move.get('depth')<bestmove.get('depth'):
                    bestmove['score'] = move.get('score') 
                    bestmove['x'] = i
                    bestmove['y'] = j
                    bestmove['depth'] = move.get('depth')
print(bestmove)