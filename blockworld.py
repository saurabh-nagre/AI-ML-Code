# Block world problem


final_state = [['a','c'],['d','b']]

# Functions to print the operations
def pickup(block):
    print('Pickup(',block,')')
def putdown(block):
    print('Putdown(',block,')')
def unstack(block1,block2):
    print('Unstack(',block1,',',block2,')')
def stack(block1,block2):
    print('stack(',block1,',',block2,')')



# put all the blocks on ground
def putBlocksonGround(input_state):
    
    for i in range(0,len(input_state)):
        if(len(input_state[i])>1):
            block = input_state[i].pop()
            pickup(block)
            putdown(block)
            input_state.append([block])
        while(len(input_state[i])>1):
            block1 = input_state[i].pop()
            unstack(block1,input_state[i][-1])
            putdown(block1)
            input_state.append([block1])
                        
def buildFinalState(input_state):

    for i in range(0,len(final_state)):
        index = input_state.index([final_state[i][0]])
        for j in range(1,len(final_state[i])):
            block1 = final_state[i][j]
            pickup(block1)
            input_state.remove([block1])
            stack(block1,final_state[i][j-1])
            input_state[index].append(block1)


# start
input_state = [['a','b','c'],['d']]
print('Input list before applying methods')
print(input_state,'\n')

putBlocksonGround(input_state)

buildFinalState(input_state)

# input state as final state
print('\ninput state as final state')

print(input_state)